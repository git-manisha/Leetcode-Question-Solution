# Write your MySQL query statement below

select person_name from(
select person_name , sum(weight) over(order by turn) 
as Total_weight from Queue) a
where a.Total_weight in
(select max(b.Total_weight) as weights from
(select sum(weight) 
    over(order by turn) as Total_weight 
    from Queue) b 
    where b.Total_weight <= 1000);


