# Write your MySQL query statement below
with new as(
select employee_id,count(employee_id) as cnt
from Employee
group by employee_id
)
select n.employee_id,e.department_id
from new as n
join
Employee as e
on n.employee_id = e.employee_id
where n.cnt =1 or e.primary_flag='Y';
