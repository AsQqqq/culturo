from database.dibs import database_query
from database import database_query_user_place
import secrets
from main_index import trash_setting


def select_all_place():
    """Берём все анкеты из global базы"""
    sql = f"SELECT * FROM places"
    cursor = database_query(sql_query=sql, types="return")
    exist = cursor.fetchall()
    return exist


def select_all_user(username: str):
    """Берём все анкеты из local базы"""
    sql = f"SELECT * FROM {username}"
    cursor = database_query_user_place(sql_query=sql, types="return")
    exist = cursor.fetchall()
    return exist


def generate_hex_place(username: str):
    """Генерация токена для place в базу данных пользователя"""
    code = f"{secrets.token_hex(16)}"
    sql = f"SELECT * FROM {username} WHERE record_id = '{code}'"
    cursor = database_query_user_place(sql_query=sql, types="return")
    existing_entry = cursor.fetchone()
    if existing_entry:
        generate_hex_place()
        return
    return code


def add_user_place(user_id: str, place_id: str, username: str):
    """Добовление place в базу данных пользователя"""
    record_id = generate_hex_place(username=username)
    sql = f"SELECT * FROM {username} WHERE place_id = '{place_id}'"
    cursor = database_query_user_place(sql_query=sql, types="return")
    rows = cursor.fetchall()
    if not rows:
        sql = f"INSERT INTO {username} (place_id, user_id, record_id) VALUES ('{place_id}', '{user_id}', '{record_id}')"
        database_query_user_place(sql_query=sql, types="none")


def confirm_trash_place_user(place_id: str, choice: str, username: str):
    """Система лайка и дизлайка"""
    if choice == "confirm":
        sql = f"SELECT estimation FROM {username} WHERE place_id = '{place_id}'"
        cursor = database_query_user_place(sql_query=sql, types="return")
        row = cursor.fetchone()
        int_row = float(row[0])
        if int_row <= 4.85:
            int_row_now = int_row + trash_setting
            sql = f"UPDATE {username} SET estimation = '{int_row_now}' WHERE place_id = '{place_id}'"
            database_query_user_place(sql_query=sql, types="none")
        sql = f"UPDATE {username} SET liked = true WHERE liked = false AND place_id = '{place_id}'"
        database_query_user_place(sql_query=sql, types="none")
    elif choice == "trash":
        sql = f"SELECT estimation FROM {username} WHERE place_id = '{place_id}'"
        cursor = database_query_user_place(sql_query=sql, types="return")
        row = cursor.fetchone()
        int_row = float(row[0])
        print(int_row)
        if int_row >= 1.15:
            int_row_now = int_row - trash_setting
            sql = f"UPDATE {username} SET estimation = '{int_row_now}' WHERE place_id = '{place_id}'"
            database_query_user_place(sql_query=sql, types="none")

    sql = f"SELECT request FROM {username} WHERE place_id = '{place_id}'"
    cursor = database_query_user_place(sql_query=sql, types="return")
    row = cursor.fetchone()
    int_row = int(row[0])
    int_row_now = int_row + 1
    sql = f"UPDATE {username} SET request = '{int_row_now}' WHERE place_id = '{place_id}'"
    database_query_user_place(sql_query=sql, types="none")


def select_no_liked_local(username: str):
    sql = f"SELECT place_id, estimation FROM {username} WHERE liked = false"
    cursor = database_query_user_place(sql_query=sql, types="return")
    exist = cursor.fetchall()
    return exist


def select_all_local(username: str):
    sql = f"SELECT place_id, estimation FROM {username}"
    cursor = database_query_user_place(sql_query=sql, types="return")
    exist = cursor.fetchall()
    return exist


def select_all_info_from_local(username: str, place_id: str):
    sql = f"SELECT * FROM {username} WHERE place_id = '{place_id}'"
    cursor = database_query_user_place(sql_query=sql, types="return")
    exist = cursor.fetchone()
    return exist


def select_id_from_global():
    sql = f"SELECT estimation, id_point FROM places"
    cursor = database_query(sql_query=sql, types="return")
    exist = cursor.fetchall()
    return exist


def select_all_info_from_global(place_id: str):
    sql = f"SELECT * FROM places WHERE id_point = '{place_id}'"
    cursor = database_query(sql_query=sql, types="return")
    exist = cursor.fetchall()
    return exist


"""
API
"""

def get_all_place_api():
    sql = f"SELECT * FROM places"
    cursor = database_query(sql_query=sql, types="return")
    exist = cursor.fetchall()
    return exist


def generate_code():
    code = f"{secrets.token_hex(16)}-{secrets.token_hex(16)}-{secrets.token_hex(16)}"
    return code


def generate_api(username: str):
    """Генерация проверочного кода"""
    code = generate_code()

    copy_query = f"SELECT * FROM accounts WHERE token = '{code}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()

    if existing_entry:
        generate_api(username=username)
        return

    sql = f"UPDATE accounts SET token = '{code}' WHERE username = '{username}'"
    database_query(sql, "none")



def check_validate_token(token: str):
    copy_query = f"SELECT * FROM accounts WHERE token = '{token}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()

    if existing_entry:
        return True

    return False


def active_token(username: str):
    copy_query = f"SELECT token FROM accounts WHERE username = '{username}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()
    print(existing_entry)

    if str(existing_entry[0]) != "None":
        return existing_entry[0]
    return "Здесь будет ваш токен"


def active_token_api(username: str):
    copy_query = f"SELECT token FROM accounts WHERE username = '{username}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()
    print(existing_entry)

    if str(existing_entry[0]) != "None":
        return True
    return False


def active_token_project(username: str):
    copy_query = f"SELECT token FROM accounts WHERE username = '{username}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()
    print(existing_entry)

    if str(existing_entry[0]) != "None":
        return True
    return False