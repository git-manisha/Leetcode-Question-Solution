# Write your MySQL query statement below

with new as(
    select e.* from Employees as e
    join
    Employees as ee
    where e.reports_to = ee.employee_id
)
select a.employee_id,
        a.name,
        count(n.reports_to) as reports_count,
        round((sum(n.age)/count(n.age))) as average_age
        from new as n
join Employees as a
on n.reports_to = a.employee_id
group by n.reports_to
order by a.employee_id;
