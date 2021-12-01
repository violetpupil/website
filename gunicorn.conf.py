wsgi_app = "app:app"
accesslog = "-"
bind = "0.0.0.0"
worker_class = "uvicorn.workers.UvicornWorker"
