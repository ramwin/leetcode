USE leetcode;
DROP TABLE Employee;
CREATE TABLE Employee (
    Id INTEGER,
    Salary INTEGER
);

INSERT INTO Employee (Id, Salary) values
(1, 100),
(2, 200),
(3, 300);

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        select Salary from Employee order by Salary desc limit N -1, 1
    );
END
