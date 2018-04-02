--show orderID, date, and shipper from associated table
Select
	OrderID,
	convert(date,OrderDate),
	CompanyName
From Orders o
JOIN Shippers s
	ON o.ShipVia=s.ShipperID