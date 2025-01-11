# Write your MySQL query statement below
with new as (
select teacher_id,subject_id as cnt
from Teacher
group by teacher_id,subject_id
)select teacher_id,count(teacher_id) as cnt
from new
group by teacher_id;