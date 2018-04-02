--Show employee and order detail info for all orders
Select
	e.EmployeeID,
	e.LastName,
	o.OrderID,
	p.ProductName,
	od.Quantity
from Employees e
join Orders o
	on o.EmployeeID = e.EmployeeID
join OrderDetails od
	on od.OrderID = o.OrderID 
join Products p
	on p.ProductID = od.ProductID 