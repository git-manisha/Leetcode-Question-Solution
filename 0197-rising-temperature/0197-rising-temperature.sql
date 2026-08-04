# Write your MySQL query statement below
select a.id as Id
from Weather as a
join Weather as b
where DATEDIFF(a.recordDate,b.recordDate) = 1
and a.temperature > b.temperature 