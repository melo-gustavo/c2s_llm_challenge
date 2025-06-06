from groq import Groq
from sqlalchemy.orm import Session
from sqlalchemy.sql import text

from db.db import session_scope
from settings import settings

client = Groq(api_key=settings.GROQ_API_KEY)


class GroqCloud:
    @staticmethod
    def invoke_llm(search: str):
        prompt = f"""
                Você é um especialista em carros e suas montadoras. Através de
                um de texto você irá identificar qual é o a coluna da minha
                tabela e uma consulta SQL para que eu possa buscar em meu banco
                (TODAS as respostas DEVEM ser convertidas para inglês).

                O nome da minha tabela é: "cars".

                Meu modelo com exemplos:

                    manufacturer: str = "Ford"
                    model: str = "Mustang"
                    power: str = "3.0"
                    fuel_type: "GASOLINE" | "ETHANOL" | "DIESEL" | "ELECTRIC"
                    | "HYBRID"
                    color: str = "Red"
                    ports_number: int = 4
                    transmission: "MANUAL" | "AUTOMATIC"
                    price: float = 50000.0
                    year: int = 2022


                {search.title()}

                Gere **apenas** uma consulta SQL em string PURA para ser
                realizada no SQLAlchemy (sem nenhuma explicação ou texto
                adicional).
            """

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content

    @staticmethod
    def search_query_in_db(session: Session, query: str | None):
        if not query:
            return None

        string_filtered = query.replace("```sql", "").replace("```", "")

        result = session.execute(text(string_filtered))
        return result.mappings().all()


# FOR RUNNING ONLY FILE #
if __name__ == "__main__":
    response = GroqCloud.invoke_llm("INSERT HERE YOU SEARCH")

    with session_scope() as session:
        result = GroqCloud.search_query_in_db(session, response)
        if result:
            for item in result:
                print(f"""
                    Car Identification: {item.car_identification}
                    Manufacturer: {item.manufacturer}
                    Model: {item.model}
                    Power: {item.power}
                    Color: {item.color}
                    Transmission: {item.transmission}
                    Fuel Type: {item.fuel_type}
                    Year: {item.year}
                    Price: {item.price}
                """)
