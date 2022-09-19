import random
import time
import json
from random_messages import generate_message 
from kafka import KafkaProducer
from datetime import datetime

# message will be serialized as json
def serializer(message):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers = ['localhost:9092'],
    value_serializer = serializer
)

if __name__== '__main__':

    while True:

        dummy_message = generate_message()

        print(f'Producing Messages @ {datetime.now()} || Message : {str(dummy_message)} ')

        producer.send('messages', dummy_message)

        time.sleep(random.randint(1,11))

        
