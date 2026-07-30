# Write your MySQL query statement below
with customer as (
    select v.customer_id,t.visit_id
    from Visits as v
    left join Transactions as t
    on v.visit_id = t.visit_id
)
select customer_id,count(customer_id) as count_no_trans
from customer
where visit_id is null
group by customer_id
