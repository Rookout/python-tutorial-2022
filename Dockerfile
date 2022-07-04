FROM python:3.9-slim

RUN mkdir /app
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py ./
COPY run.py ./
COPY models/item.py ./models/item.py

ENTRYPOINT gunicorn run:tutorial_app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080