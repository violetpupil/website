FROM python:3.8-alpine
WORKDIR /backend
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "gunicorn" ]