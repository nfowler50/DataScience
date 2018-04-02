--Return three countries with highest average freight in 2015
Select Top 3
	ShipCountry,
	AverageFreight=avg(freight)
from Orders
Where YEAR(OrderDate)=2015
Group by ShipCountry
Order by AverageFreight desc

