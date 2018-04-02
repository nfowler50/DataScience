--find number of products in each category
Select
	CategoryName,
	count(*)
From Categories c
Join Products p
	ON c.CategoryID=p.CategoryID
Group by CategoryName
Order by count(*) desc