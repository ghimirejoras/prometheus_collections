FROM python:3.7-slim

RUN pip install prometheus_client
RUN pip install flask
RUN pip install prometheus-flask-exporter

RUN echo "Prometheus prometheus_client installed with Flask app running on port 5000"

ENV LISTEN_PORT=5000

EXPOSE 5000

COPY app /app

WORKDIR /app

CMD ["python", "wsgi_prom.py"]

