# Write your MySQL query statement below


with new_tbl as(
select a.machine_id,(a.timestamp-aa.timestamp) as tmp
from Activity as a
inner join Activity as aa
where a.machine_id=aa.machine_id
    and a.process_id=aa.process_id
    and a.timestamp>aa.timestamp
)
select machine_id,round(sum(tmp)/count(machine_id),3) as processing_time
from new_tbl
group by machine_id;


