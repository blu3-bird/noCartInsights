## Exploratory Data Analysis (EDA)

### dataset overview

- **source**: brazilian olist public dataset (kaggle)
- **records**: ~99,441 orders
- **period**: oct 2016 - oct 2018
- **tables**: 8 raw tables + 3 featured tables

---

### univariate analysis

#### order_status

```
delivered      97.02%
shipped         1.11%
canceled        0.63%
unavailable     0.61%
invoiced        0.32%
processing      0.30%
created         0.01%
approved        0.00%
```

**insight**: overwhelming majority of orders are delivered successfully.

#### is_delayed

```
on-time    91.89%
delayed     8.11%
```

**insight**: ~8% orders arrive later than estimated delivery date.

#### is_repeat_customer

```
new        93.62%
repeat      6.38%
```

**insight**: low customer retention - most buyers purchase only once.

#### delivery_days

| stat   | value                |
| ------ | -------------------- |
| mean   | 11.6 days            |
| median | 9 days               |
| min    | -7 days (data error) |
| max    | 208 days (outlier)   |
| std    | 9.5 days             |

**insight**: most orders delivered within 6-15 days. few extreme outliers exist.

#### order_value

| stat   | value  |
| ------ | ------ |
| mean   | R$ 160 |
| median | R$ 100 |

**insight**: right-skewed distribution - few high-value orders pull up the average.

---

### bivariate analysis

#### review_score vs is_delayed

| group   | avg review |
| ------- | ---------- |
| on-time | 4.3        |
| delayed | 2.6        |

**statistical test**: t-test confirms significant difference (p ≈ 0, t = 89.2)

**insight**: delivery delays severely hurt customer satisfaction.

#### top 10 categories by revenue

1. bed_bath_table
2. health_beauty
3. sports_leisure
4. computers_accessories
5. furniture_decor
6. housewares
7. watches_gifts
8. auto
9. toys
10. office_furniture

**insight**: home/lifestyle categories dominate revenue.

#### payment_type distribution

```
credit_card     ~75%
boleto          ~20%
voucher          ~3%
debit_card       ~2%
```

**insight**: credit card is the dominant payment method.

---

### monthly trends

- orders grew from oct 2016 to aug 2018
- peak month: november 2017 (~8,300 orders)
- decline in sep-oct 2018 (incomplete data)

---

### key takeaways

1. **delivery performance matters** - delays directly impact reviews
2. **low retention** - only 7% repeat customers, opportunity for improvement
3. **home categories lead** - bed_bath_table is the top revenue driver
4. **credit card dominance** - 75% of all payments
5. **seasonal pattern** - orders peak in nov-jan (holiday season)
