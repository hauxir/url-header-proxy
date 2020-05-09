FROM python:3.6-slim

RUN pip install flask requests gunicorn flask_limiter flask_cors

# BitTorrent incoming
EXPOSE 5000

COPY app /app

WORKDIR /app

CMD python app.py
