



"""
   ____ ___  _   _ _____ ____   ___  _        ____    _  _____  _    ____    _    ____  _____ 
  / ___/ _ \| \ | |_   _|  _ \ / _ \| |      |  _ \  / \|_   _|/ \  | __ )  / \  / ___|| ____|
 | |  | | | |  \| | | | | |_) | | | | |      | | | |/ _ \ | | / _ \ |  _ \ / _ \ \___ \|  _|  
 | |__| |_| | |\  | | | |  _ <| |_| | |___   | |_| / ___ \| |/ ___ \| |_) / ___ \ ___) | |___ 
  \____\___/|_| \_| |_| |_| \_\\___/|_____|  |____/_/   \_\_/_/   \_\____/_/   \_\____/|_____|

"""

# Импорт модулей flask
from psycopg2 import connect, Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from decoding import get_database_config_main # , get_database_config_place
from flask_login import UserMixin


def connected_database_main() -> tuple[connect, connect]:
    "Функция для подключения к главной базе данных"
    try:
        connection: connect = connect(
            user=get_database_config_main()[0],
            password=get_database_config_main()[2],
            host=get_database_config_main()[1],
            port=get_database_config_main()[3],
            database=get_database_config_main()[4]
        )
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        return connection, cursor
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


# def connected_database_places() -> tuple[connect, connect]:
#     "Функция для подключения к базе данных мест"
#     try:
#         connection: connect = connect(
#             user=get_database_config_place()[0],
#             password=get_database_config_place()[2],
#             host=get_database_config_place()[1],
#             port=get_database_config_place()[3],
#             database=get_database_config_place()[4]
#         )
#         connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#         cursor = connection.cursor()
#         return connection, cursor
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)


def closing_database(cursor, connection):
    "Функция для закрытия соединения с базой данных"
    cursor.close()
    connection.close()
    print("Соеденение с PostgreSQL закрыто")


def database_query(sql_query: str, types: str) -> connect or None:
    "Функция для выполнения запроса к главной базе данных"
    connection, cursor = connected_database_main()

    cursor.execute(sql_query)
    
    if types == "return":
        return cursor
    
    closing_database(cursor=cursor, connection=connection)


# def database_query_user_place(sql_query: str, types: str) -> connect or None:
#     "Функция для выполнения запроса к базе данных мест"
#     connection, cursor = connected_database_places()

#     cursor.execute(sql_query)
    
#     if types == "return":
#         return cursor
    
#     closing_database(cursor=cursor, connection=connection)


class User(UserMixin):
    "Класс пользователя"
    def __init__(self, user_id):
        self.id = user_id
