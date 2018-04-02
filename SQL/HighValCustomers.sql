--We want to send all of our high-value customers a special VIP gift. We're defining high-
--value customers as those who've made at least 1 order with a total value (not including the
--discount) equal to $10,000 or more. We only want to consider orders made in the year 2016.

Select
	C.CustomerID,
	C.CompanyName,
	O.OrderID,
	TotalAmount=SUM(Od.UnitPrice*Od.Quantity)
from Customers C
Join Orders O on C.CustomerID=O.CustomerID
Join OrderDetails Od on O.OrderID=Od.OrderID

Where YEAR(O.OrderDate)=2016
Group by C.CustomerID, C.CompanyName, O.OrderID

Having SUM(Od.UnitPrice*Od.Quantity)>10000

Order by TotalAmount Desc