--The Northwind mobile app developers would now like to just get a random assortment of
--orders for beta testing on their app. Show a random set of 2% of all orders.

Select top 2 percent
	OrderID
from Orders

Order by NewID()