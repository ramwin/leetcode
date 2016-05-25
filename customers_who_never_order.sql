select Name as Customers from Customers where Id not in (select Customers.Id from Customers, Orders where Customers.Id = Orders.CustomerId);
