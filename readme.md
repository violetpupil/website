```
docker build -t instafever/backend .
docker push instafever/backend
```

```
docker run -dp 8000:8000 --name backend_prod instafever/backend
```