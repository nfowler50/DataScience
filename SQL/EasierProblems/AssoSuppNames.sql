--Show productID, product name, and supplier from related table
Select
	ProductID,
	ProductName,
	Supplier=CompanyName
From Products
JOIN
	Suppliers
ON Products.SupplierID=Suppliers.SupplierID