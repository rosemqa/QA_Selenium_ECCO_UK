from dataclasses import dataclass


@dataclass
class Address:
    street: str
    building_number: str
    post_code: str
    city: str
