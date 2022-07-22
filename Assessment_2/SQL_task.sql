---This is a SQL task---
SELECT a.author_name, SUM(b.sold_copies) as sold
FROM AUTHORS a 
LEFT JOIN BOOKS b
ON a.Book_name=b.book_name
GROUP BY a.author_name
ORDER BY sold
LIMIT 3;  