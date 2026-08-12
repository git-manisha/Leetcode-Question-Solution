# Write your MySQL query statement below
with manager as (
    select managerId,count(managerId) as reports from Employee
    group by managerId
)
select e.name
from manager as m
join Employee as e
on m.managerId = e.id
where reports >= 5