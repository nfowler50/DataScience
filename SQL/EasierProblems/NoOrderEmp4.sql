-- show customers who have never placed an order with Margaret Peacokc, Employee ID 4
Select
	c.CustomerID,
	o.CustomerID
from Customers c
	left join Orders o
		on o.CustomerID=c.CustomerID and EmployeeID=4
Where o.CustomerID is NULL