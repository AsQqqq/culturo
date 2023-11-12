from psycopg2 import connect
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from decoding import get_database_place, get_database_user
from flask_login import UserMixin


def connected_database_place():
    try:
        connection: connect = connect(user=get_database_place()[0],
                            password=get_database_place()[2],
                            host=get_database_place()[1],
                            port=get_database_place()[3],
                            database=get_database_place()[4])
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        return connection, cursor
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def connected_database_user():
    try:
        connection: connect = connect(user=get_database_user()[0],
                            password=get_database_user()[2],
                            host=get_database_user()[1],
                            port=get_database_user()[3],
                            database=get_database_user()[4])
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        return connection, cursor
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


def closing_database(cursor, connection):
    cursor.close()
    connection.close()
    print("Соеденение с PostgreSQL закрыто")


def database_query(sql_query: str, types: str):
    """Функция для запросов в базу данных"""
    connection, cursor = connected_database_place()

    cursor.execute(sql_query)
    
    if types == "return":
        return cursor
    
    closing_database(cursor=cursor, connection=connection)


def database_query_user_place(sql_query: str, types: str):
    """Функция для запросов в базу данных"""
    connection, cursor = connected_database_user()

    cursor.execute(sql_query)
    
    if types == "return":
        return cursor
    
    closing_database(cursor=cursor, connection=connection)


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id