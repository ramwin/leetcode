use leetcode;
drop table Weather;
create table Weather (
    Id integer,
    Date date not null,
    Temperature integer
);
insert into Weather values(1, "2015-01-16", 3);
insert into Weather values(2, "2015-01-15", -1);
-- insert into Weather values(3, "2015-01-03", 20);
-- insert into Weather values(4, "2015-01-04", 30);

select b.Id from Weather a, Weather b where b.Date = DATE_ADD(a.Date, INTERVAL 1 DAY) and a.Temperature < b.Temperature;
