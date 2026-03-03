# Write your MySQL query statement below
/*select s.student_id,s.student_name,e.subject_name,count(*) as attended_exams
from Students as s
left join 
(
select e.student_id,s.subject_name
from Examinations as e
inner join Subjects as s
on e.subject_name = s.subject_name
) as e
on s.student_id = e.student_id
group by 1,2,3
*/

select s.student_id,s.student_name,e.subject_name,count() as attended_exams
from Examinations as e
right join
(
select s.student_id,s.student_name,s2.subject_name
from Students as s
cross join Subjects as s2
) as s
on e.student_id = s.student_id
and e.subject_name = s.subject_name
group by s.student_id,s.subject_name

