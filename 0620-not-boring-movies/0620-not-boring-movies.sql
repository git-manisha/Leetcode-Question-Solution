# Write your MySQL query statement below

 select * from Cinema
 where description not in ("boring") and id%2!=0
 order by rating desc;