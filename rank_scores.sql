use leetcode;
drop table Scores;
create table Scores (
    Id integer,
    Score Float
);
# insert into Scores values
#     (1, "3.50"),
#     (2, "3.65"),
#     (3, "4.00"),
#     (4, "3.85"),
#     (5, "4.00"),
#     (6, "3.65");
insert into Scores values
    (1, "1.00"),
    (2, "1.00"),
    (3, "0.99");

select
    Score,
    (select count(*) from (
        select count(Score) c, Score aaa
        from Scores
        group by Score
        order by Score desc) tmp
    where Score < aaa)+1 Rank
from Scores
order by Score desc;
