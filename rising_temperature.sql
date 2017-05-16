use leetcode;
drop table rising_temperature;
create table rising_temperature (
    Id integer,
    Date date not null,
    Temperature integer
);
insert into rising_temperature values(1, "2015-01-16", 3);
insert into rising_temperature values(2, "2015-01-15", -1);
-- insert into rising_temperature values(3, "2015-01-03", 20);
-- insert into rising_temperature values(4, "2015-01-04", 30);

select b.Id from rising_temperature a, rising_temperature b where a.Date = b.Date-1 and a.Temperature < b.Temperature;
