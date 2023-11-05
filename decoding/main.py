from dotenv import load_dotenv
from os import environ
load_dotenv()


def get_database_main() -> tuple:
    """Получения данных о основном аккаунте"""
    DATABASE_LOGIN_MAIN = environ["DATABASE_LOGIN_MAIN"]
    DATABASE_URL = environ["DATABASE_URL"]
    DATABASE_PASSWORD_MAIN = environ["DATABASE_PASSWORD_MAIN"]
    DATABASE_PORT = environ["DATABASE_PORT"]
    DATABASE = environ["DATABASE"]
    return DATABASE_LOGIN_MAIN, DATABASE_URL, \
            DATABASE_PASSWORD_MAIN, DATABASE_PORT, DATABASE


def get_database_place() -> tuple:
    """Получения данных о входном аккаунте"""
    DATABASE_LOGIN_PLACE = environ["DATABASE_LOGIN_PLACE"]
    DATABASE_URL = environ["DATABASE_URL"]
    DATABASE_PASSWORD_PLACE = environ["DATABASE_PASSWORD_PLACE"]
    DATABASE_PORT = environ["DATABASE_PORT"]
    DATABASE = environ["DATABASE"]
    return DATABASE_LOGIN_PLACE, DATABASE_URL, \
            DATABASE_PASSWORD_PLACE, DATABASE_PORT, DATABASE