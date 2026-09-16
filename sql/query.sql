-- total revenue

select sum(total_amount) from featured_order_items


-- total Orders

select count(order_id) as total_orders,
	count(order_id) filter (where order_status = 'delivered') as total_delivered_orders
	from orders

    -- total customers
 select count(*) as total_customers from customers 

 -- total sellers

select count(*) as total_sellers from sellers

-- avg order value
select avg(amount) as avg_order_value from order_payments

-- avg review score

select avg(review_score) as avg_review_score from order_reviews