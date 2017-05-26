use leetcode;
drop table World;
create table World (
    name varchar(255),
    continent varchar(255),
    area integer,
    population integer,
    gdp integer
);
insert into World (name, continent, area, population, gdp) values 
('Afghanistan', 'Asia', 652230, 25500100, 20343000),
('Afghanistan', 'Asia', 652230, 25500100, 20343001);

select name, population, area from World where (area > 3000000) or population > 25000000;
