import random
import uuid

from sqlalchemy.orm import Session

from db.db import session_scope
from mocks.faker_providers import FakerProvider, fake
from models.car import Car
from schemas.car import CarSchema


class Faker:
    @staticmethod
    def create_car_objects(db: Session, count=100):
        cars = []
        for _ in range(count):
            manufacturer = fake.manufacturers()
            car_data = {
                "car_identification": uuid.uuid4(),
                "manufacturer": manufacturer,
                "model": random.choice(
                    FakerProvider.manufacturers_models[manufacturer]),
                "power": FakerProvider.generate_power_car(),
                "fuel_type": fake.fuel_types(),
                "color": fake.color_name(),
                "ports_number": fake.ports_number(),
                "transmission": fake.transmission_types(),
                "year": FakerProvider.generate_year(),
                "price": FakerProvider.generate_price_car(),
            }
            validated_data = CarSchema(**car_data).model_dump()
            cars.append(Car(**validated_data))

        db.bulk_save_objects(cars)
        db.commit()
        return len(cars)


# FOR RUNNING ONLY FILE #
if __name__ == "__main__":
    with session_scope() as session:
        Faker.create_car_objects(session, 100)
