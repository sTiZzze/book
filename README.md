SELECT * FROM book \
WHERE book.created_date BETWEEN 2023-01-01 00:00:00+00:00 AND 2024-08-29 00:00:00+00:00 \
ORDER BY book.pages DESC;