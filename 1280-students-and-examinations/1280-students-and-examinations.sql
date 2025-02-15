# Write your MySQL query statement below

with new_tbl as (
select s.student_id , s.student_name, s1.subject_name
from Students as s
cross join Subjects as s1
)
select n.student_id,n.student_name,
        n.subject_name,count(e.student_id) as attended_exams
from new_tbl as n 
left join Examinations as e
on n.student_id=e.student_id
    and n.subject_name = e.subject_name
group by n.student_id,n.subject_name
order by n.student_id,n.subject_name;




