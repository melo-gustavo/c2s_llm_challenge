from db.db import session_scope
from services.groq_cloud import GroqCloud
from tests import YEAR


class TestGroqCloud:
    @staticmethod
    def test_input_user_llm():
        response = GroqCloud.invoke_llm("Carro preto")
        assert response is not None

        assert "SELECT" in response
        assert "color = 'Black'" or 'color = "Black"' in response

    @staticmethod
    def test_input_user_llm_error():
        response = GroqCloud.invoke_llm("Carro preto com ano acima de 2020")
        assert response is not None

        assert "SELECT" in response
        assert "color = 'Black'" or 'color = "Black"' in response
        assert "year > 2025" in response

    @staticmethod
    def test_input_search_manufacturer():
        response = GroqCloud.invoke_llm("Carro com ano acima de 2020")
        assert isinstance(response, str)

        with session_scope() as session:
            result = GroqCloud.search_query_in_db(session, response)
            assert result is not None

            found = False
            if result:
                for item in result:
                    if item.year > YEAR:
                        found = True
                        break
                assert found

    @staticmethod
    def test_input_search_manufacturer_error():
        response = GroqCloud.invoke_llm("Carro com ano acima de 2030")
        assert isinstance(response, str)

        with session_scope() as session:
            result = GroqCloud.search_query_in_db(session, response)
            assert result

            found = False
            if result:
                for item in result:
                    if item.model.lower() == "tesla 3":
                        found = True
                        break
                assert found

    @staticmethod
    def test_input_search_aleatory():
        response = GroqCloud.invoke_llm("Qualquer carro da volkswagen")
        assert isinstance(response, str)

        with session_scope() as session:
            result = GroqCloud.search_query_in_db(session, response)
            assert result is not None

            found = False
            if result:
                for item in result:
                    if item.manufacturer.lower() == "volkswagen":
                        found = True
                        break
                assert found

    @staticmethod
    def test_input_search_aleatory_error():
        response = GroqCloud.invoke_llm("carro rx7")
        assert isinstance(response, str)

        with session_scope() as session:
            result = GroqCloud.search_query_in_db(session, response)
            assert result

            found = False
            if result:
                for item in result:
                    if item.model.lower() == "rx7":
                        found = True
                        break
                assert not found
