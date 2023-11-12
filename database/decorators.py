from database.dibs import database_query

def get_testing(user_id: str):
    sql_query = f"SELECT tested FROM accounts WHERE user_id = '{user_id}'"
    cursror = database_query(sql_query=sql_query, types="return")
    result = cursror.fetchone()
    return result[0]

def replace_tested_changed(user_id: str):
    sql_query = f"UPDATE accounts SET tested = true WHERE user_id = '{user_id}' AND tested = false"
    database_query(sql_query=sql_query, types="none")


def replace_add_tested_location(user_id: str, location: str):
    sql_query = f"UPDATE accounts SET common_location = '{location}' WHERE user_id = '{user_id}' AND tested = true"
    database_query(sql_query=sql_query, types="none")