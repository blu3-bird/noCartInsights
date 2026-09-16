-- monthly wise order count
--select * from featured_orders
select date_trunc('month',delivered_customer_date) as order_month, 
 		sum(order_count) as order_count
from featured_orders
filter where( order_status = 'delivered')
group by date_trunc('month',delivered_customer_date)
order by order_count desc;


-- Top 10 products by total revenue

select p.product_id, p.category_name,
sum(oi.freight_value) as total_revenue
from orders_items oi
join products p
on oi.product_id = p.product_id

group by p.product_id, p.category_name
order by total_revenue desc
limit 10



-- avg review score by order_status
select o.order_status,
round(avg(r.review_score),2) as avg_review_score
from orders o
join order_reviews r
on o.order_id = r.order_id
group by o.order_status
order by avg_review_score


-- top 10 customers by order_value
select c.customer_unique_id,
sum(fo.order_value) as total_order_value
from featured_orders fo
join customers c
on fo.customer_unique_id = c.customer_unique_id
where (fo.order_status = 'delivered')
group by c.customer_unique_id

order by total_order_value desc
limit 10


-- -- cash orders and credits orders
select payment_type , count(order_id) as order_count
from order_payments
group by payment_type
order by order_count desc


-- avg review score by repeat customer
select fo.is_repeat_customer, avg(r.review_score) as avg_review_score
from featured_orders fo
join order_reviews r
on fo.order_id = r.order_id
group by fo.is_repeat_customer



-- customer spending by categories
select fo.customer_unique_id, sum(foi.total_amount) as total_spending
from featured_orders fo
join featured_order_items foi
on fo.order_id = foi.order_id
group by fo.customer_unique_id
order by total_spending desc
limit 10;


-- ranking state by spending
select c.customer_state, c.customer_city, sum(fo.order_value) as spending
from customers c
join featured_orders fo
on c.customer_unique_id = fo.customer_unique_id
where fo.order_status = 'delivered'
group by c.customer_state  , c.customer_city
order by spending desc
limit 15


-- top sellers
select s.seller_id, round(sum(oi.price):: numeric ,2) as total_revenue
from sellers s
join orders_items oi
on s.seller_id = oi.seller_id
group by s.seller_id
order by total_revenue desc
limit 10;


-- sellers performance
select s.seller_id, count(oi.order_id) as order_count
from sellers s
join orders_items oi
on s.seller_id = oi.seller_id
group by s.seller_id
order by order_count desc
limit 10;