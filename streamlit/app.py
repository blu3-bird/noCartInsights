import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="noCartInsights", page_icon="📊", layout="wide")


@st.cache_data
def load_data():
    data_dir = Path(__file__).parent.parent / "data" / "feature_engineered"
    clean_dir = Path(__file__).parent.parent / "data" / "cleaned"
    orders = pd.read_csv(data_dir / "featured_orders.csv")
    items = pd.read_csv(data_dir / "featured_order_items.csv")
    products = pd.read_csv(data_dir / "featured_products.csv")
    reviews = pd.read_csv(clean_dir / "cleaned_order_reviews.csv")
    return orders, items, products, reviews


orders, items, products, reviews = load_data()
delivered = orders[orders["order_status"] == "delivered"].copy()

# sidebar
st.sidebar.title("noCartInsights")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "go to",
    [
        "home",
        "sales analysis",
        "customer analysis",
        "seller analysis",
        "delivery analysis",
    ],
)
st.sidebar.markdown("---")
st.sidebar.caption("Brazilian olist Dataset")

# home
if page == "home":
    st.title("ecommerce performance dashboard")
    st.markdown("key metrics from **brazilian olist** dataset")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("total orders", f"{len(orders):,}")
    with c2:
        st.metric("total revenue", f" {orders['order_value'].sum():,.0f}")
    with c3:
        st.metric("total customers", f"{orders['customer_unique_id'].nunique():,}")
    with c4:
        st.metric("avg order value", f" {orders['order_value'].mean():.2f}")

    st.markdown("---")

    left, right = st.columns(2)

    with left:
        st.subheader("order status")
        status_counts = orders["order_status"].value_counts()
        fig = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        fig.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("monthly orders")
        orders["month"] = pd.to_datetime(orders["order_purchase"]).dt.to_period("M")
        monthly = orders.groupby("month").size().reset_index(name="count")
        monthly["month"] = monthly["month"].astype(str)
        fig = px.area(monthly, x="month", y="count")
        st.plotly_chart(fig, use_container_width=True)

# sales
elif page == "sales analysis":
    st.title("sales analysis")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("total revenue", f" {delivered['order_value'].sum():,.0f}")
    with c2:
        st.metric("avg order value", f" {delivered['order_value'].mean():.2f}")
    with c3:
        st.metric("total items sold", f"{len(items):,}")

    st.markdown("---")

    st.subheader("monthly revenue trend")
    delivered["month"] = pd.to_datetime(
        delivered["delivered_customer_date"]
    ).dt.to_period("M")
    monthly = (
        delivered.groupby("month")["order_value"].agg(["sum", "count"]).reset_index()
    )
    monthly["month"] = monthly["month"].astype(str)
    fig = px.line(
        monthly,
        x="month",
        y="sum",
        markers=True,
        labels={"sum": "revenue", "month": "month"},
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("top 10 categories by revenue")
    merged = items.merge(products[["product_id", "category_name_eng"]], on="product_id")
    cat_rev = (
        merged.groupby("category_name_eng")["total_amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig = px.bar(
        cat_rev,
        x="category_name_eng",
        y="total_amount",
        color="total_amount",
        color_continuous_scale="Blues",
    )
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

# customer
elif page == "customer analysis":
    st.title("customer analysis")

    repeat_custs = (
        orders.groupby("is_repeat_customer")["customer_unique_id"]
        .nunique()
        .reset_index()
    )
    repeat_custs.columns = ["repeat", "count"]
    repeat_custs["repeat"] = repeat_custs["repeat"].map({0: "new", 1: "repeat"})

    c1, c2 = st.columns(2)
    with c1:
        st.metric("total customers", f"{orders['customer_unique_id'].nunique():,}")
    with c2:
        repeat_pct = (
            repeat_custs[repeat_custs["repeat"] == "repeat"]["count"].values[0]
            / repeat_custs["count"].sum()
            * 100
        )
        st.metric("repeat customer rate", f"{repeat_pct:.1f}%")

    st.markdown("---")

    left, right = st.columns(2)

    with left:
        st.subheader("new vs repeat customers")
        fig = px.pie(
            repeat_custs,
            values="count",
            names="repeat",
            color_discrete_sequence=["#667eea", "#764ba2"],
        )
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("top 10 customers by spending")
        top_cust = (
            orders[orders["order_status"] == "delivered"]
            .groupby("customer_unique_id")["order_value"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )
        fig = px.bar(
            top_cust,
            x="customer_unique_id",
            y="order_value",
            color="order_value",
            color_continuous_scale="Purples",
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

# seller
elif page == "seller analysis":
    st.title("seller analysis")

    seller_stats = (
        items.groupby("seller_id")
        .agg(total_revenue=("total_amount", "sum"), order_count=("order_id", "nunique"))
        .reset_index()
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("total sellers", f"{seller_stats['seller_id'].nunique():,}")
    with c2:
        st.metric(
            "avg revenue per seller", f"R$ {seller_stats['total_revenue'].mean():,.0f}"
        )
    with c3:
        st.metric("avg orders per seller", f"{seller_stats['order_count'].mean():.1f}")

    st.markdown("---")

    left, right = st.columns(2)

    with left:
        st.subheader("top 10 sellers by revenue")
        top_sellers = seller_stats.sort_values("total_revenue", ascending=False).head(
            10
        )
        fig = px.bar(
            top_sellers,
            x="seller_id",
            y="total_revenue",
            color="total_revenue",
            color_continuous_scale="Greens",
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("orders per seller")
        fig = px.histogram(
            seller_stats, x="order_count", nbins=40, color_discrete_sequence=["#2ecc71"]
        )
        st.plotly_chart(fig, use_container_width=True)

# delivery
elif page == "delivery analysis":
    st.title("delivery analysis")

    delayed_reviews = delivered.merge(
        reviews[["order_id", "review_score"]], on="order_id", how="inner"
    )
    ontime_score = delayed_reviews[delayed_reviews["is_delayed"] == 0][
        "review_score"
    ].mean()
    delayed_score = delayed_reviews[delayed_reviews["is_delayed"] == 1][
        "review_score"
    ].mean()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("avg delivery days", f"{delivered['delivery_days'].mean():.1f}")
    with c2:
        st.metric("median delivery days", f"{delivered['delivery_days'].median():.1f}")
    with c3:
        st.metric("delay rate", f"{delivered['is_delayed'].mean() * 100:.1f}%")
    with c4:
        st.metric("review gap", f"{ontime_score - delayed_score:.2f}")

    st.markdown("---")

    left, right = st.columns(2)

    with left:
        st.subheader("delivery days distribution")
        fig = px.histogram(
            delivered, x="delivery_days", nbins=30, color_discrete_sequence=["#3498db"]
        )
        fig.update_layout(xaxis_title="days", yaxis_title="orders")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.subheader("delay vs on-time review score")
        avg_reviews = (
            delayed_reviews.groupby("is_delayed")["review_score"].mean().reset_index()
        )
        avg_reviews["is_delayed"] = avg_reviews["is_delayed"].map(
            {0: "on time", 1: "delayed"}
        )
        fig = px.bar(
            avg_reviews,
            x="is_delayed",
            y="review_score",
            color="is_delayed",
            color_discrete_sequence=["#2ecc71", "#e74c3c"],
        )
        fig.update_layout(yaxis_title="avg review score")
        st.plotly_chart(fig, use_container_width=True)
