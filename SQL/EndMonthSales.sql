--At the end of the month, salespeople are likely to try much harder to get orders, to meet
--their month-end quotas. Show all orders made on the last day of the month. Order by 
--EmployeeID and OrderID

Select
	EmployeeID,
	OrderID,
	convert(date,OrderDate)
from Orders

Where OrderDate=EOMonth(OrderDate)
Order by EmployeeID, OrderID
