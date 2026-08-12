# Write your MySQL query statement below

with student as (
    select *
    from Students as s
    cross join Subjects as t
)
select s.student_id,s.student_name,s.subject_name,count(e.subject_name) as attended_exams
from student as s
left join Examinations as e
on s.student_id = e.student_id 
and s.subject_name = e.subject_name
group by s.student_id,s.subject_name
order by s.student_id,s.subject_name