# Write your MySQL query statement below

with new_class as (
select class,count(student) as cnt
from Courses
group by class
) select class from new_class
where cnt>=5;