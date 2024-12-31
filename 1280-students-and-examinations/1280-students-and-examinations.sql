# Write your MySQL query statement below

with new_table as(
    select * from Students 
    cross join Subjects
)
select n.student_id,
    n.student_name,
    n.subject_name,
    count(e.subject_name) as attended_exams
     from new_table as n
left join Examinations as e 
on n.student_id = e.student_id
and n.subject_name = e.subject_name
group by n.student_id,n.subject_name
order by n.student_id,n.subject_name;