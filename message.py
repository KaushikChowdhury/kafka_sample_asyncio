from dataclasses import dataclass, field
from faker import Faker
import json

faker = Faker()

@dataclass
class Purchase:
    username: str = field(default_factory=faker.user_name)
    currency: str = field(default_factory=faker.currency_code)
    uri: str = field(default_factory=faker.uri)

    def serialize(self):
        return json.dumps(
            {
                'username': self.username,
                'currency': self.currency,
                'uri': self.uri
            }
        )

    @classmethod
    def deserialize(cls, json_str):

        purchase_json = json.loads(json_str)

        return Purchase(
            username = purchase_json['username'],
            currency = purchase_json['currency'],
            uri = purchase_json['uri'],
        )




