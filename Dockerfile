FROM python:3.9.13-slim

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py ./
COPY run.py ./
COPY models/item.py ./models/item.py
COPY static ./static

ENTRYPOINT gunicorn run:main --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8080 --preload