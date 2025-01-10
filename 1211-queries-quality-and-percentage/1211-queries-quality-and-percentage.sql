# Write your MySQL query statement below
with new as(
select query_name,
        (rating/position) as pos,
        case
        when rating<3 then 1 else 0
        end as poor
        from Queries
)
select query_name,
        round(sum(pos)/count(query_name),2) as quality,
        round((sum(poor)/count(query_name))*100,2) as poor_query_percentage
        from new
        group by 1;
        