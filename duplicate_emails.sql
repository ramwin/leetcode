use leetcode;
drop table Person;
create table Person (
    Id integer,
    Email varchar(255)
);
insert into Person values(1, 'a@b.com');
insert into Person values(2, 'c@d.com');
insert into Person values(3, 'a@b.com');
select Email from Person group by Email having count(*) > 1;
