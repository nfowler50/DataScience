--display products which need to be reordered
Select
	ProductID,
	ProductName,
	UnitsInStock,
	UnitsOnOrder,
	ReorderLevel,
	Discontinued
From Products
Where (UnitsInStock+UnitsOnOrder)<=ReorderLevel and Discontinued=0