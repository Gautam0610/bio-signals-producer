
import time
import random
import os
from kafka import KafkaProducer
import json

def generate_vitals():
    heart_rate = random.randint(60, 100)  # Normal range
    breaths_per_minute = random.randint(12, 20)  # Normal range
    body_temperature = round(random.uniform(36.5, 37.5), 1)  # Normal range in Celsius
    blood_pressure_systolic = random.randint(90, 120)  # Normal range
    blood_pressure_diastolic = random.randint(60, 80)  # Normal range
    oxygen_saturation = random.randint(95, 100)  # Normal range

    # Introduce occasional extreme values
    if random.random() < 0.05:  # 5% chance
        heart_rate = random.randint(150, 220)  # Extreme heart rate
    if random.random() < 0.05:
        breaths_per_minute = random.randint(30, 50)  # Extreme breaths per minute

    return {
        "heart_rate": heart_rate,
        "breaths_per_minute": breaths_per_minute,
        "body_temperature": body_temperature,
        "blood_pressure_systolic": blood_pressure_systolic,
        "blood_pressure_diastolic": blood_pressure_diastolic,
        "oxygen_saturation": oxygen_saturation
    }

def main():
    kafka_topic = os.environ.get("OUTPUT_TOPIC")
    kafka_bootstrap_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    
    producer = KafkaProducer(
        bootstrap_servers=kafka_bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    if not kafka_topic:
        print("Error: OUTPUT_TOPIC environment variable not set.")
        return

    while True:
        vitals = generate_vitals()
        print(f"Sending: {vitals}")
        producer.send(kafka_topic, value=vitals)
        time.sleep(1)

if __name__ == "__main__":
    main()
