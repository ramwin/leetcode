use leetcode;
drop table Person;
drop table Address;
create table Person (
    PersonId integer,
    FirstName varchar(255),
    LastName varchar(255)
    );
create table Address (
    AddressId integer,
    PersonId integer,
    City varchar(255),
    State varchar(255)
    );

insert into Person values (1, 'a', 'A');
insert into Person values (2, 'b', 'B');
insert into Person values (3, 'c', 'C');
insert into Person values (4, 'd', 'D');
insert into Person values (5, 'e', 'E');
insert into Person values (6, 'f', 'F');


insert into Address values (1, 1, 'city1', 'state1');
insert into Address values (2, 2, 'city2', 'state2');
insert into Address values (3, 4, 'city3', 'state3');
insert into Address values (4, 6, 'city4', 'state4');

select * from Person where Person.PersonId not in (select PersonId from Address);
-- select FirstName, LastName, City, State from Person, Address where Person.PersonId = Address.PersonId or (Person.PersonId not in (select PersonId from Address));
