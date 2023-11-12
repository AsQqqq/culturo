from database.dibs import database_query

def get_testing(user_id: str):
    sql_query = f"SELECT tested FROM accounts WHERE user_id = '{user_id}'"
    cursror = database_query(sql_query=sql_query, types="return")
    result = cursror.fetchone()
    return result[0]