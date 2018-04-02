--Recalculate high value customers (as in the previous problem) including discounts in the calculation.

Select
	C.CustomerID,
	C.CompanyName,
	TotalAmount=SUM(Od.UnitPrice*Od.Quantity*(1-Od.Discount))
from Customers C
Join Orders O on C.CustomerID=O.CustomerID
Join OrderDetails Od on O.OrderID=Od.OrderID

Where YEAR(O.OrderDate)=2016
Group by C.CustomerID, C.CompanyName
Having SUM(Od.UnitPrice*Od.Quantity)>15000

Order by TotalAmount Desc