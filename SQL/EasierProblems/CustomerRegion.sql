--list customers by region, ordering by customer id, placing all entries with no region at end of list
Select
	CustomerID,
	CompanyName,
	Region
from Customers
Order by
	Case
		when Region is null then 1
		else 0
	End,
	Region,
	CustomerID