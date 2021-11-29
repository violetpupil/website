wsgi_app = "app:app"
accesslog = "access.log"
errorlog = "error.log"
daemon = True
pidfile = "pid"
bind = "0.0.0.0"
worker_class = "uvicorn.workers.UvicornWorker"
