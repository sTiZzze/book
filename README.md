## SQL query:
```
SELECT * FROM book 
WHERE book.created_date BETWEEN 2023-01-01 00:00:00+00:00 AND 2024-08-29 00:00:00+00:00
ORDER BY book.pages DESC;
```

## Urls

Access to admin: http://localhost:8000/admin/

Access to api: http://localhost:8000/api/

### Auth

Create access token: http://localhost:8000/api/token/

Refresh access token: http://localhost:8000/api/token/refresh/

### Books

Manage issues: http://localhost:8000/api/library/


## Run linter

```
make lint
```