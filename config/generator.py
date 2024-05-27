from faker import Faker
from config.data import Address

fake = Faker('en_GB')


def generated_address():
    return Address(
        street=fake.street_name(),
        building_number=fake.building_number(),
        post_code=fake.postcode(),
        city=fake.city()
    )
