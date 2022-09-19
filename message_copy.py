from dataclasses import dataclass, field
from faker import Faker
import json

faker = Faker()

class ClickEvent:

    def __init__(self):
        self.email = faker.email()
        self.timestamp = faker.iso8601()
        self.uri = faker.uri()

    def serialize(self):
        
        val = json.dumps({
            'email': self.email,
            'timestamp': self.timestamp,
            'uri': self.uri
        })

        return val

    def deserialize(self,json_data):

        return ClickEvent(json.loads(json_data))
        