from contextlib import contextmanager

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

from settings import settings


class Base(DeclarativeBase):
    pass


POSTGRE_URL_DB = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
engine = create_engine(POSTGRE_URL_DB)


def create_database_if_not_exists():
    try:
        conn = psycopg2.connect(
            dbname=settings.DB_NAME_DEFAULT,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
            port=settings.DB_PORT
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(f"""
            SELECT 1 FROM pg_database WHERE datname = '{settings.DB_NAME}'""")
        if not cur.fetchone():
            cur.execute(f"CREATE DATABASE {settings.DB_NAME}")
            print(f"Banco '{settings.DB_NAME}' criado.")
        cur.close()
        conn.close()
    except Exception as e:
        print("Erro ao criar banco:", e)


@contextmanager
def session_scope():
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
