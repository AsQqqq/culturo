from database.dibs import database_query
from database import database_query_user_place
import secrets
from main_index import trash_setting


def count_all_accounts():
    sql = "SELECT COUNT(id) FROM accounts WHERE save = true"
    cursor = database_query(sql_query=sql, types="return")
    result = cursor.fetchone()[0]
    return result

def count_all_places():
    sql = "SELECT COUNT(id) FROM places"
    cursor = database_query(sql_query=sql, types="return")
    result = cursor.fetchone()[0]
    return result