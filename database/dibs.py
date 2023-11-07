from psycopg2 import connect
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from decoding import get_database_main, get_database_place

def debugs():
    print(get_database_main())
    print(type(get_database_main()))
    print(get_database_place())
    print(type(get_database_place()))

def connected_database_main():
    try:
        connection: connect = connect(user=get_database_main()[0],
                            password=get_database_main()[2],
                            host=get_database_main()[1],
                            port=get_database_main()[3],
                            database=get_database_place()[4])
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        return connection, cursor
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)


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


def closing_database(cursor, connection):
    cursor.close()
    connection.close()
    print("Соеденение с PostgreSQL закрыто")


def database_query(sql_query: str, users: str, types: str):
    """Функция для запросов в базу данных"""
    if users == "place":
        connection, cursor = connected_database_place()
    else:
        connection, cursor = connected_database_main()

    cursor.execute(sql_query)
    
    if types == "return":
        return cursor
    
    closing_database(cursor=cursor, connection=connection)