--show total number customer per Country and City
Select
	Country,
	City,
	TotalCustomer=count(*)
From Customers
Group by Country,City
Order by count(*) desc