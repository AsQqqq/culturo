from database.dibs import database_query
from database import database_query_user_place
import secrets
from main_index import trash_setting


def select_all_place():
    sql = f"SELECT * FROM places"
    cursor = database_query(sql_query=sql, types="return")
    exist = cursor.fetchall()
    return exist


def select_all_user(username: str):
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
        int_row = int(row[0])
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
        int_row = int(row[0])
        if int_row >= 1.15:
            int_row_now = int_row - trash_setting
            sql = f"UPDATE {username} SET estimation = '{int_row_now}' WHERE place_id = '{place_id}'"
            database_query_user_place(sql_query=sql, types="none")
