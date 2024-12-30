# Write your MySQL query statement below

with activity_new as(
    select a1.machine_id,(a1.timestamp-a2.timestamp) as p 
    from Activity as a1
    join Activity as a2
    where a1.machine_id = a2.machine_id
    and a1.process_id = a2.process_id 
    and a1.timestamp > a2.timestamp
)
select machine_id,round(avg(p),3) as processing_time
from activity_new
group by 1;
