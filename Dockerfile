FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY bio_signals_producer.py .

ENV OUTPUT_TOPIC="vitals-topic"

CMD ["python", "bio_signals_producer.py"]