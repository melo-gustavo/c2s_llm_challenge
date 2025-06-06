import random
import uuid

from pytest_schema import exact_schema

from mocks.faker_providers import FakerProvider, fake
from schemas.car import CarSchema
from tests import FOUR_PORTS, TWO_PORTS


class TestPopulateDB:
    @staticmethod
    def test_create_car_objects():
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
        assert exact_schema(car_data) == CarSchema(**car_data).model_dump()

    @staticmethod
    def test_create_car_objects_error():
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
        }

        assert exact_schema(car_data) == CarSchema(**car_data).model_dump()

    @staticmethod
    def test_fuel_types():
        result = fake.fuel_types()
        assert ("Gasoline" or "Ethanol" or "Diesel"
            or "Electric" or "Hybrid" in result)

    @staticmethod
    def test_fuel_types_error():
        result = fake.fuel_types()
        assert "Gasoline/Ethanol" in result

    @staticmethod
    def test_get_model_manufacturer():
        result = FakerProvider.get_model_for_manufacturer("Audi")
        assert isinstance(result, str)

    @staticmethod
    def test_get_model_manufacturer_error():
        result = FakerProvider.get_model_for_manufacturer("Audi")
        assert isinstance(result, int)

    @staticmethod
    def test_generate_power():
        result = FakerProvider.generate_power_car()
        assert isinstance(result, float)

    @staticmethod
    def test_generate_power_error():
        result = FakerProvider.generate_power_car()
        assert isinstance(result, str)

    @staticmethod
    def test_generate_price():
        result = FakerProvider.generate_price_car()
        assert isinstance(result, float)

    @staticmethod
    def test_generate_price_error():
        result = FakerProvider.generate_price_car()
        assert isinstance(result, int)

    @staticmethod
    def test_get_manufacturers():
        result = fake.manufacturers()
        assert isinstance(result, str)

    @staticmethod
    def test_get_manufacturers_error():
        result = fake.manufacturers()
        assert isinstance(result, int)

    @staticmethod
    def test_transmission_types():
        result = fake.transmission_types()
        assert "Manual" or "Automatic" in result

    @staticmethod
    def test_transmission_types_error():
        result = fake.transmission_types()
        assert "Manual/Automatic" in result

    @staticmethod
    def test_ports_number():
        result = fake.ports_number()
        assert TWO_PORTS or FOUR_PORTS in result

    @staticmethod
    def test_ports_number_error():
        result = fake.ports_number()
        assert isinstance(result, bool)
