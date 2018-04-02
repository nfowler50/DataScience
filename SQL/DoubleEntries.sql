--Janet Leverling, one of the salespeople, has come to you with a request. She thinks that she
--accidentally entered a line item twice on an order, each time with a different ProductID, but
--the same quantity. She remembers that the quantity was 60 or more. Show all the OrderIDs
--with line items that match this, in order of OrderID.

Select OrderID,
	Quantity
from OrderDetails
Where Quantity>=60

Group by OrderID, Quantity
Having count(*)>1

Order by OrderID