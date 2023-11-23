



"""
  ____  _____ ____ ___  ____ ___ _   _  ____ 
 |  _ \| ____/ ___/ _ \|  _ \_ _| \ | |/ ___|
 | | | |  _|| |  | | | | | | | ||  \| | |  _ 
 | |_| | |__| |__| |_| | |_| | || |\  | |_| |
 |____/|_____\____\___/|____/___|_| \_|\____|

"""

# Импорт необходимых модулей
from dotenv import load_dotenv
from os import environ
from typing import Tuple

# Загрузка переменных окружения из файла .env
load_dotenv()


def get_database_config_main() -> Tuple[str, str]:
    "Получение данных для входа в основную базу данных"
    DATABASE_LOGIN_PLACE = environ["LOGIN_MAIN"]
    DATABASE_URL = environ["DATABASE_URL"]
    DATABASE_PASSWORD_PLACE = environ["PASSWORD_MAIN"]
    DATABASE_PORT = environ["DATABASE_PORT"]
    DATABASE = environ["DATABASE_NAME"]
    return DATABASE_LOGIN_PLACE, DATABASE_URL, \
            DATABASE_PASSWORD_PLACE, DATABASE_PORT, DATABASE


# def get_database_config_place() -> Tuple[str, str]:
#     "Получения данных для входа в дополнительную базу данных"
#     DATABASE_LOGIN_PLACE = environ["LOGIN_PLACE"]
#     DATABASE_URL = environ["DATABASE_URL"]
#     DATABASE_PASSWORD_PLACE = environ["PASSWORD_MAIN"]
#     DATABASE_PORT = environ["DATABASE_PORT"]
#     DATABASE = environ["DATABASE_NAME"]
#     return DATABASE_LOGIN_PLACE, DATABASE_URL, \
#             DATABASE_PASSWORD_PLACE, DATABASE_PORT, DATABASE


def get_config_server() -> Tuple[str, str]:
    "Получение данных для создания сервера FLASK"
    IP = environ["IP"]
    PORT = environ["PORT"]
    return IP, PORT
