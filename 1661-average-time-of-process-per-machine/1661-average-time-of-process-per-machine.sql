# Write your MySQL query statement below
with start as (
    select * from Activity where activity_type = 'start'
),
end as (
    select * from Activity where activity_type = 'end'
)
select s.machine_id ,round(sum((e.timestamp-s.timestamp))/count(s.machine_id),3) as processing_time
from start as s
join end as e
where s.machine_id = e.machine_id
and s.process_id = e.process_id
group by s.machine_id