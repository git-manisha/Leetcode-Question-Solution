# Write your MySQL query statement below
select w.id
from Weather as w
inner join Weather as ww 
where datediff(w.recordDate, ww.recordDate) = 1
and w.temperature > ww.temperature;