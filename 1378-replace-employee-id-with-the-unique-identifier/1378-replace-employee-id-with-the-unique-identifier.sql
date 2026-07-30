# Write your MySQL query statement below

select a.unique_id,e.name
from Employees as e
left join EmployeeUNI as a
on e.id = a.id;