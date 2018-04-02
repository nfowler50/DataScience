-- show customers who have never placed an order
Select
	c.CustomerID,
	o.CustomerID
from Customers c
	left join Orders o
		on o.CustomerID=c.CustomerID
Where o.CustomerID is NULL