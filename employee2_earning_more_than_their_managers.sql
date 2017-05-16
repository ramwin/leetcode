use leetcode;
drop table Employee;
create table Employee (
    Id integer,
    Name varchar(255),
    Salary integer,
    ManagerId integer
);
insert into Employee values(1, 'Joe', 70000, 3);
insert into Employee values(2, 'Six', 80000, 4);
insert into Employee values(3, 'May', 60000, NULL);
insert into Employee values(4, 'Max', 90000, NULL);

select a.name Employee from Employee a left join Employee b ON a.managerid = b.Id where a.Salary > b.Salary;
