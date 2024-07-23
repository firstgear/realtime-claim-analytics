from kafka import KafkaProducer
from datetime import datetime
import json
import time
import random
import logging
import os

# Get the environment variable
my_kafka_server = os.getenv('KAFKA_SERVER')

logging.basicConfig(level=logging.INFO)

def create_kafka_producer():
    while True:
        try:
            producer = KafkaProducer(
#                bootstrap_servers=['kafka:9092'],
                bootstrap_servers=[my_kafka_server],
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            logging.info("Kafka producer created successfully")
            return producer
        except Exception as e:
            logging.error(f"Error creating Kafka producer: {e}")
            time.sleep(5)

#time.sleep(30)
#replaced by dynamic kafka healthcheck in docker compose

producer = create_kafka_producer()

def generate_data():
    while True:
        data = {
        'timestamp': datetime.now().isoformat(),
        'claim_type': random.choice(insurance_claim_types),
        'fraud_score': random.choice(fraud_scores),
        'claim_value': random.choice(claim_values)
        }
        producer.send('insurance-claims', data)
        logging.info(f'Sent: {data}')
        time.sleep(1)

if __name__ == "__main__":

    insurance_claim_types = ['car', 'home', 'health']
    fraud_scores = range(1, 100)
    claim_values = range(1000, 10000)

    generate_data()
