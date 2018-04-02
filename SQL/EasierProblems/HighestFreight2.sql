--three highest freight charges in last 12 months
Select Top 3
	ShipCountry,
	AverageFreight=avg(freight)
from Orders
Where OrderDate between '2015-05-06' and '2016-05-06'
Group by ShipCountry
Order by AverageFreight desc