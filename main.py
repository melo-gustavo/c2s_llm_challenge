import subprocess

from db.db import create_database_if_not_exists, session_scope
from mocks.populate_db import Faker
from models.car import Car
from services.groq_cloud import GroqCloud


def init_project_dependencies():
    create_database_if_not_exists()

    subprocess.run(["alembic", "upgrade", "head"], check=True)

    with session_scope() as session:
        if not session.query(Car).first():
            Faker.create_car_objects(session, 100)


def run():
    first_search = True

    while True:
        print("Seja bem vindo ao agente virtual da C2S Cars."
            if first_search else "")
        search = str(
            input(
                """Digite qual carro você deseja buscar: """
                if first_search
                else "Deseja continuar? Informe o carro ou 'exit' para sair: "
            )
        )

        if search == "exit":
            first_search = False
            break
        else:
            response = GroqCloud.invoke_llm(search)

            if not response:
                raise Exception("Desculpe, nenhum carro encontrado!")

            with session_scope() as session:
                all_cars = GroqCloud.search_query_in_db(session, response)
                if all_cars is not None:
                    for car in all_cars:
                        print(f"""
                            Car Identification": {car.car_identification}
                            Manufacturer: {car.manufacturer}
                            Model: {car.model}
                            Power: {car.power}
                            Color: {car.color}
                            Transmission: {car.transmission}
                            Fuel Type: {car.fuel_type}
                            Year: {car.year}
                            Price: {car.price}
                            """)
            first_search = False

    print("Até logo!")


if __name__ == "__main__":
    init_project_dependencies()
    run()
