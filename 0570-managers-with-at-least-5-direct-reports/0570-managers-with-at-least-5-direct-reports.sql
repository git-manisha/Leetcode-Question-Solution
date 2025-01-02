# Write your MySQL query statement below
with cte as(
    select managerId,count(managerID) as mng_count
    from Employee
    where managerId is not null
    group by managerId
)select e.name from cte as c
left join Employee as e 
on c.managerId = e.id
where mng_count>=5;