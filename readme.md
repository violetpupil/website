```
docker build -t instafever/backend .
docker push instafever/backend
```

```
docker run -dp 8000:8000 --name backend_pro instafever/backend
docker run -dp 8000:8000 --name backend_dev instafever/backend uvicorn app:app --reload --host 0.0.0.0
```