# Write your MySQL query statement below

select p.product_id,ifnull(round(sum(p.price*s.units)/sum(s.units),2),0) as average_price from
UnitsSold as s
join
Prices as p
on p.product_id = s.product_id and
s.purchase_date>=p.start_date and s.purchase_date<=p.end_date
group by p.product_id
