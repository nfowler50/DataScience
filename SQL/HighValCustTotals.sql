--The manager has changed their mind. Instead of requiring that customers have at least one
--individual orders totaling $10,000 or more, they want to define high-value customers as
--those who have orders totaling $15,000 or more in 2016. How would you change the
--answer to the previous problem?

Select
	C.CustomerID,
	C.CompanyName,
	TotalAmount=SUM(Od.UnitPrice*Od.Quantity)
from Customers C
Join Orders O on C.CustomerID=O.CustomerID
Join OrderDetails Od on O.OrderID=Od.OrderID

Where YEAR(O.OrderDate)=2016
Group by C.CustomerID, C.CompanyName
Having SUM(Od.UnitPrice*Od.Quantity)>15000

Order by TotalAmount Desc