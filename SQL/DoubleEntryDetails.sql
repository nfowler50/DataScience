--Based on the previous problem (finding double entries), we now want to show details of the order,
--for orders that match the preceding criteria

;with PotentialDuplicates as (
Select OrderID
from OrderDetails
Where Quantity>=60

Group by OrderID, Quantity
Having count(*)>1
)

Select * from OrderDetails
Where OrderID in (Select OrderID from PotentialDuplicates)

Order by OrderID, Quantity