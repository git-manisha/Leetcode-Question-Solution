# Write your MySQL query statement below
select machine_id,round((sum(timep)/count(process_id)),3) as processing_time
from (
select a1.machine_id,a1.process_id,abs(a1.timestamp - a2.timestamp) as timep
from Activity as a1
inner join Activity as a2
where a1.process_id = a2.process_id
and a1.machine_id = a2.machine_id
group by a1.machine_id,a1.process_id
) as sample
group by machine_id