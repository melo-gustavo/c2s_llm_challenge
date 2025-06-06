import random

from faker import Faker
from faker.providers import DynamicProvider

fake = Faker()


class FakerProvider:
    @staticmethod
    def get_model_for_manufacturer(manufacturer):
        return random.choice(
            FakerProvider.manufacturers_models[manufacturer])

    @staticmethod
    def generate_power_car():
        return str(round(random.uniform(1.0, 10.0), 1))

    @staticmethod
    def generate_price_car():
        return round(random.uniform(10000.0, 1000000.0), 2)

    @staticmethod
    def generate_year():
        return random.randint(2010, 2025)

    manufacturers_models = {
        "Ford": ["Focus", "Fusion", "Mustang"],
        "General Motors": ["Cadillac Escalade", "Chevrolet Cruze",
            "GMC Sierra"],
        "Volkswagen": ["Golf", "Polo", "Passat"],
        "Lamborghini": ["Aventador", "Huracán", "Urus"],
        "Jaguar": ["XE", "XF", "F-PACE"],
        "Toyota": ["Corolla", "Hilux", "Fortuner"],
        "Honda": ["Civic", "Accord", "HR-V"],
        "BMW": ["320i", "X5", "i3"],
        "Mercedes-Benz": ["C-Class", "E-Class", "GLA"],
        "Audi": ["A3", "A4", "Q5"],
        "Nissan": ["Sentra", "Altima", "Kicks"],
        "Hyundai": ["HB20", "Creta", "Tucson"],
        "Kia": ["Seltos", "Sportage", "Cerato"],
        "Renault": ["Kwid", "Duster", "Sandero"],
        "Peugeot": ["208", "2008", "3008"],
        "Fiat": ["Uno", "Argo", "Toro"],
        "Chevrolet": ["Onix", "Tracker", "S10"],
        "Subaru": ["Impreza", "XV", "Forester"],
        "Mazda": ["Mazda3", "CX-5", "MX-5"],
        "Tesla": ["Model S", "Model 3", "Model X"],
    }

    manufacturers = DynamicProvider(
        provider_name="manufacturers",
        elements=list(manufacturers_models.keys())
    )

    fuel_types = DynamicProvider(
        provider_name="fuel_types",
        elements=["Gasoline", "Ethanol", "Diesel", "Electric", "Hybrid"],
    )

    transmission_types = DynamicProvider(
        provider_name="transmission_types",
        elements=["Manual", "Automatic"],
    )

    ports_number = DynamicProvider(
        provider_name="ports_number",
        elements=[2, 4],
    )

    fake.add_provider(fuel_types)
    fake.add_provider(transmission_types)
    fake.add_provider(ports_number)
    fake.add_provider(manufacturers)
