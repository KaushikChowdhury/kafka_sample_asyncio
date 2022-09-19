import time
from confluent_kafka import Producer, Consumer
from confluent_kafka.admin import AdminClient
from message import Purchase
import asyncio
import json

BROKER_URL = 'PLAINTEXT://localhost:9092'

async def produce(topic_name):
    p = Producer({'bootstrap.servers': BROKER_URL})

    while True:
        event = Purchase()
        p.produce(topic_name, event.serialize())
        print(f"Producer: {event.serialize()}")
        await asyncio.sleep(5.0)


async def consume(topic_name):
    c = Consumer({'bootstrap.servers': BROKER_URL, 'group.id': 'faker-gp'})
    c.subscribe([topic_name])
    while True:
        message = c.poll(0.0)

        if message is None:
            print('No message received')
        else:
            pur_json = json.loads(message.value())
            print(f"Consumer: {Purchase(pur_json['username'],pur_json['currency'],pur_json['uri'])}")
        await asyncio.sleep(2.0)


async def produce_consume(topic_name):
    t1 = asyncio.create_task(produce(topic_name))
    t2 = asyncio.create_task(consume(topic_name))
    await t1
    await t2


def main():
    client = AdminClient({'bootstrap.servers': BROKER_URL})
    asyncio.run(produce_consume('faker'))

if __name__=='__main__':
    main()