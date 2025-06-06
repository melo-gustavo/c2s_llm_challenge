import uuid

from pydantic import BaseModel


class CarSchema(BaseModel):
    car_identification: uuid.UUID
    manufacturer: str
    model: str
    power: str
    fuel_type: str
    color: str
    ports_number: int
    transmission: str
    year: int
    price: float
