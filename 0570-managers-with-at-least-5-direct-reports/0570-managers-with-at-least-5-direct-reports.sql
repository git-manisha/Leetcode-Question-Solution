# Write your MySQL query statement below

select name 
from (
select e1.name,e1.id,count(e2.managerId) as mng
from Employee as e1
join Employee as e2
where e1.id =e2.managerId
group by e1.id
)t
where mng>=5;


 


