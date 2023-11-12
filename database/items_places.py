from .dibs import database_query


def get_data_database_testing():
    sql_query=f"SELECT common_location FROM places"
    cursor = database_query(sql_query=sql_query, types="return")
    data = cursor.fetchall()
    return data