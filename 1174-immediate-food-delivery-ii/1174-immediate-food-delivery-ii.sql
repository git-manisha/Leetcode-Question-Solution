# Write your MySQL query statement below
with new as (
select customer_id,min(order_date) as ord_date,customer_pref_delivery_date 
    from Delivery
    group by customer_id
)
select round((sum(
        case when ord_date = customer_pref_delivery_date then 1 else 0 end
        )/(select count(distinct customer_id) from Delivery))*100,2)
    as immediate_percentage
    from new;

