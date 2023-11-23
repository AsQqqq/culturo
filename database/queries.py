



"""
   ___  _   _ _____ ____  ___ _____ ____  
  / _ \| | | | ____|  _ \|_ _| ____/ ___| 
 | | | | | | |  _| | |_) || ||  _| \___ \ 
 | |_| | |_| | |___|  _ < | || |___ ___) |
  \__\_\\___/|_____|_| \_\___|_____|____/ 

"""

from database.control_database import database_query # , database_query_user_place
import secrets
from config import estimation
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime


"""
 _____ _____ _____ _____ _____ ____       _____ _____ _____ _____ 
|_   _|   __|   __|_   _|   __|    \     |  _  |  _  | __  |_   _|
  | | |   __|__   | | | |   __|  |  |    |   __|     |    -| | |  
  |_| |_____|_____| |_| |_____|____/     |__|  |__|__|__|__| |_| 

"""


def get_testing(user_id: str):
    """Получение этапа тестирования из базы данных пользователя"""
    sql_query = f"SELECT tested FROM accounts WHERE user_id = '{user_id}'"
    cursror = database_query(sql_query=sql_query, types="return")
    result = cursror.fetchone()
    return result[0]


def user_testing_changed(user_id: str):
    """Обновления тестирования в базе данных пользователя"""
    sql_query = f"UPDATE accounts SET tested = true WHERE user_id = '{user_id}' AND tested = false"
    database_query(sql_query=sql_query, types="none")


def add_common_location_from_test(user_id: str, location: str):
    """Добовляем локацию которую выбрал себе пользователь"""
    sql_query = f"UPDATE accounts SET common_location = '{location}' WHERE user_id = '{user_id}' AND tested = true"
    database_query(sql_query=sql_query, types="none")


def get_common_location_from_test():
    """Читаем локацию которую выбрал пользователь"""
    sql_query=f"SELECT common_location FROM places"
    cursor = database_query(sql_query=sql_query, types="return")
    data = cursor.fetchall()
    return data


"""
 _ _____ ____  _____ __ __ 
|_|   | |    \|   __|  |  |
| | | | |  |  |   __|-   -|
|_|_|___|____/|_____|__|__|

"""


# def select_all_users_from_places():
#     """Берём все анкеты из global базы"""
#     sql = f"SELECT * FROM places"
#     cursor = database_query(sql_query=sql, types="return")
#     exist = cursor.fetchall()
#     return exist


# def select_all_user(username: str):
#     """Берём все анкеты из local базы"""
#     sql = f"SELECT * FROM {username}"
#     cursor = database_query_user_place(sql_query=sql, types="return")
#     exist = cursor.fetchall()
#     return exist


# def generate_hex_place(username: str):
#     """Генерация токена для place в базу данных пользователя"""
#     code = f"{secrets.token_hex(16)}"
#     sql = f"SELECT * FROM {username} WHERE record_id = '{code}'"
#     cursor = database_query_user_place(sql_query=sql, types="return")
#     existing_entry = cursor.fetchone()
#     if existing_entry:
#         generate_hex_place()
#         return
#     return code


# def add_user_place(user_id: str, place_id: str, username: str):
#     """Добовление place в базу данных пользователя"""
#     record_id = generate_hex_place(username=username)
#     sql = f"SELECT * FROM {username} WHERE place_id = '{place_id}'"
#     cursor = database_query_user_place(sql_query=sql, types="return")
#     rows = cursor.fetchall()
#     if not rows:
#         sql = f"INSERT INTO {username} (place_id, user_id, record_id) VALUES ('{place_id}', '{user_id}', '{record_id}')"
#         database_query_user_place(sql_query=sql, types="none")


# def confirm_trash_place_user(place_id: str, choice: str, username: str):
#     """Система лайка и дизлайка"""
#     if choice == "confirm":
#         sql = f"SELECT estimation FROM {username} WHERE place_id = '{place_id}'"
#         cursor = database_query_user_place(sql_query=sql, types="return")
#         row = cursor.fetchone()
#         int_row = float(row[0])
#         if int_row <= 4.85:
#             int_row_now = int_row + estimation
#             sql = f"UPDATE {username} SET estimation = '{int_row_now}' WHERE place_id = '{place_id}'"
#             database_query_user_place(sql_query=sql, types="none")
#         sql = f"UPDATE {username} SET liked = true WHERE liked = false AND place_id = '{place_id}'"
#         database_query_user_place(sql_query=sql, types="none")
#     elif choice == "trash":
#         sql = f"SELECT estimation FROM {username} WHERE place_id = '{place_id}'"
#         cursor = database_query_user_place(sql_query=sql, types="return")
#         row = cursor.fetchone()
#         int_row = float(row[0])
#         print(int_row)
#         if int_row >= 1.15:
#             int_row_now = int_row - estimation
#             sql = f"UPDATE {username} SET estimation = '{int_row_now}' WHERE place_id = '{place_id}'"
#             database_query_user_place(sql_query=sql, types="none")

#     sql = f"SELECT request FROM {username} WHERE place_id = '{place_id}'"
#     cursor = database_query_user_place(sql_query=sql, types="return")
#     row = cursor.fetchone()
#     int_row = int(row[0])
#     int_row_now = int_row + 1
#     sql = f"UPDATE {username} SET request = '{int_row_now}' WHERE place_id = '{place_id}'"
#     database_query_user_place(sql_query=sql, types="none")


# def select_no_liked_local(username: str):
#     sql = f"SELECT place_id, estimation FROM {username} WHERE liked = false"
#     cursor = database_query_user_place(sql_query=sql, types="return")
#     exist = cursor.fetchall()
#     return exist


# def select_all_local(username: str):
#     sql = f"SELECT place_id, estimation FROM {username}"
#     cursor = database_query_user_place(sql_query=sql, types="return")
#     exist = cursor.fetchall()
#     return exist


# def select_all_info_from_local(username: str, place_id: str):
#     sql = f"SELECT * FROM {username} WHERE place_id = '{place_id}'"
#     cursor = database_query_user_place(sql_query=sql, types="return")
#     exist = cursor.fetchone()
#     return exist


# def select_id_from_global():
#     sql = f"SELECT estimation, id_point FROM places"
#     cursor = database_query(sql_query=sql, types="return")
#     exist = cursor.fetchall()
#     return exist


# def select_all_info_from_global(place_id: str):
#     sql = f"SELECT * FROM places WHERE id_point = '{place_id}'"
#     cursor = database_query(sql_query=sql, types="return")
#     exist = cursor.fetchall()
#     return exist



def select_all_places():
    """Выбрать все места из глобальной базы данных"""
    sql = "SELECT * FROM places"
    cursor = database_query(sql_query=sql, types="return")
    result = cursor.fetchall()
    return result


def select_user_profile(username: str):
    """Выбрать все профили из локальной базы данных"""
    sql = f"SELECT * FROM {username}"
    cursor = database_query_user_place(sql_query=sql, types="return")
    result = cursor.fetchall()
    return result


def generate_hex_token(username: str):
    """Сгенерировать токен для места в базе данных пользователя"""
    code = f"{secrets.token_hex(16)}"
    sql = f"SELECT * FROM {username} WHERE record_id = '{code}'"
    cursor = database_query_user_place(sql_query=sql, types="return")
    existing_entry = cursor.fetchone()
    if existing_entry:
        generate_hex_token(username=username)
        return
    return code


def add_user_place(user_id: str, place_id: str, username: str):
    """Добавить место в базу данных пользователя"""
    record_id = generate_hex_token(username=username)
    sql = f"SELECT * FROM {username} WHERE place_id = '{place_id}'"
    cursor = database_query_user_place(sql_query=sql, types="return")
    rows = cursor.fetchall()
    if not rows:
        sql = f"INSERT INTO {username} (place_id, user_id, record_id) VALUES ('{place_id}', '{user_id}', '{record_id}')"
        database_query_user_place(sql_query=sql, types="none")


def rate_place_user(place_id: str, choice: str, username: str):
    """Лайк или дизлайк для места"""
    if choice == "confirm":
        sql = f"SELECT estimation FROM {username} WHERE place_id = '{place_id}'"
        cursor = database_query_user_place(sql_query=sql, types="return")
        row = cursor.fetchone()
        int_row = float(row[0])
        if int_row <= 4.85:
            int_row_now = int_row + estimation
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
            int_row_now = int_row - estimation
            sql = f"UPDATE {username} SET estimation = '{int_row_now}' WHERE place_id = '{place_id}'"
            database_query_user_place(sql_query=sql, types="none")

    sql = f"SELECT request FROM {username} WHERE place_id = '{place_id}'"
    cursor = database_query_user_place(sql_query=sql, types="return")
    row = cursor.fetchone()
    int_row = int(row[0])
    int_row_now = int_row + 1
    sql = f"UPDATE {username} SET request = '{int_row_now}' WHERE place_id = '{place_id}'"
    database_query_user_place(sql_query=sql, types="none")


def select_non_liked_local(username: str):
    """Выбирает места пользователя (не понравившиеся) из локальной базы данных."""
    sql = f"SELECT place_id, estimation FROM {username} WHERE liked = false"
    cursor = database_query_user_place(sql_query=sql, types="return")
    result = cursor.fetchall()
    return result


def select_all_local_info(username: str):
    """Выбирает всю информацию о местах пользователя из локальной базы данных."""
    sql = f"SELECT place_id, estimation FROM {username}"
    cursor = database_query_user_place(sql_query=sql, types="return")
    result = cursor.fetchall()
    return result


def select_local_info(username: str, place_id: str):
    """Выбирает информацию о конкретном месте пользователя из локальной базы данных."""
    sql = f"SELECT * FROM {username} WHERE place_id = '{place_id}'"
    cursor = database_query_user_place(sql_query=sql, types="return")
    result = cursor.fetchone()
    return result


def select_global_ids():
    """Выбирает идентификаторы и оценки всех мест из глобальной базы данных."""
    sql = f"SELECT estimation, id_point FROM places"
    cursor = database_query(sql_query=sql, types="return")
    result = cursor.fetchall()
    return result


def select_global_info(place_id: str):
    """Выбирает всю информацию о конкретном месте из глобальной базы данных."""
    sql = f"SELECT * FROM places WHERE id_point = '{place_id}'"
    cursor = database_query(sql_query=sql, types="return")
    result = cursor.fetchall()
    return result


"""
 _____ _____ _____ 
|  _  |  _  |     |
|     |   __|-   -|
|__|__|__|  |_____|

"""

def get_all_place_api():
    "Чтение всего всех мест"
    sql = f"SELECT * FROM places"
    cursor = database_query(sql_query=sql, types="return")
    exist = cursor.fetchall()
    return exist


def generate_hex_token():
    "Генерация hex токена"
    code = f"{secrets.token_hex(16)}-{secrets.token_hex(16)}-{secrets.token_hex(16)}"
    return code


def generate_api(username: str):
    """Генерация проверочного кода"""
    code = generate_hex_token()

    copy_query = f"SELECT * FROM accounts WHERE token = '{code}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()

    if existing_entry:
        generate_api(username=username)
        return

    sql = f"UPDATE accounts SET token = '{code}' WHERE username = '{username}'"
    database_query(sql, "none")


def check_validate_token(token: str):
    "Проверка на эксплюзивность токена"
    copy_query = f"SELECT * FROM accounts WHERE token = '{token}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()

    if existing_entry:
        return True

    return False


def select_user_token(username: str):
    "Чтение токена пользователя"
    copy_query = f"SELECT token FROM accounts WHERE username = '{username}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()

    if str(existing_entry[0]) != "None":
        return existing_entry[0]
    return "Здесь будет ваш токен"


def check_exist_token(username: str):
    "Проверка токена в базе данных"
    copy_query = f"SELECT token FROM accounts WHERE username = '{username}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()

    if str(existing_entry[0]) != "None":
        return True
    return False





"""
 __    _____ _____ _____ _____ 
|  |  |     |   __|     |   | |
|  |__|  |  |  |  |-   -| | | |
|_____|_____|_____|_____|_|___|

"""


def check_exist_in_database_user(login: str, password: str) -> bool:
    sql_query = f"SELECT * FROM accounts WHERE username = '{login}' AND save = true"
    cursor = database_query(sql_query, "return")
    existing_entry = cursor.fetchall()
    try:
        login_base = existing_entry[0][3]
        password_base = existing_entry[0][4]
    except:
        return False
    if login_base != login and check_password_hash(password_base, password) == False:
        return False
    return True



"""


"""


def code_search_in_the_database(code: str):
    "Поиск кода в базе данных"
    sql_query = f"SELECT * FROM code WHERE code = '{code}'"
    cursor = database_query(sql_query, "return")
    existing_entry = cursor.fetchone()
    return existing_entry


def account_confirmation(code: str):
    "Подтверждение аккаунта"
    sql_query = f"UPDATE code SET activate = False WHERE code = '{code}'"
    database_query(sql_query, "none")
    code_nickname = code.split("-")[3]
    sql_query = f"UPDATE accounts SET save = True WHERE username = '{code_nickname}'"
    database_query(sql_query, "none")
    
    sql_query = f'''
        CREATE TABLE IF NOT EXISTS {code_nickname} (
            id SERIAL PRIMARY KEY,
            place_id VARCHAR(255),
            user_id VARCHAR(255),
            record_id VARCHAR(255),
            liked BOOLEAN DEFAULT (FALSE),
            estimation DOUBLE PRECISION DEFAULT (5),
            request BIGINT DEFAULT (0)
        )
    '''
    database_query_user_place(sql_query=sql_query, types="none")


def get_email(email: str):
    sql_query = f"SELECT * FROM accounts WHERE email = '{email}' AND save = false"
    cursor = database_query(sql_query, "return")
    if cursor.fetchone():
        sql_query = f"DELETE FROM accounts WHERE email = '{email}' AND save = false"
        database_query(sql_query, "none")
    sql_query = f"SELECT email FROM accounts WHERE email = '{email}' AND save = true"
    cursor = database_query(sql_query, "return")
    if cursor.fetchone():
        return True
    return False


def generate_email_token(login: str):
    "Генерация токена для почты"
    code = f"{secrets.token_hex(16)}-{secrets.token_hex(16)}-{secrets.token_hex(16)}-{login}"
    return code


def generate_verification_code(login: str):
    """Генерация проверочного кода"""
    code = generate_email_token(login=login)

    copy_query = f"SELECT * FROM code WHERE code = '{code}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()
    print(existing_entry)
    if existing_entry:
        generate_verification_code(login=login)
        return

    sql_query = f"SELECT * FROM code WHERE login = '{login}' AND activate = True"
    cursor = database_query(sql_query, "return")
    existing_entry = cursor.fetchone()

    if existing_entry: 
        sql_query = f"UPDATE code SET activate = False WHERE login = '{login}'"
        database_query(sql_query, "none")

    sql_query = f"SELECT * FROM code WHERE code = '{code}'"
    cursor = database_query(sql_query, "return")
    existing_entry = cursor.fetchone()
    
    if existing_entry:
        generate_verification_code(login=login)
        return


    sql_query = f"INSERT INTO code (code, login, activate) VALUES ('{code}', '{login}', True)"
    database_query(sql_query, "none")


def selected_verification_code(login: str) -> str:
    """Чтение проверочного кода"""
    sql_query = f"SELECT * FROM code WHERE login = '{login}'"
    cursor = database_query(sql_query, "return")
    existing_entry = cursor.fetchone()
    return str(existing_entry[1])


def generate_user_id():
    code = f"{secrets.token_hex(16)}"
    copy_query = f"SELECT * FROM accounts WHERE user_id = '{code}'"
    cursor = database_query(copy_query, "return")
    existing_entry = cursor.fetchone()
    if existing_entry:
        generate_user_id()
        return
    return code


def pre_save_account(name, surname, email, login, password):
    try:
        current_datetime = datetime.now()
        sql_query = f"INSERT INTO accounts (name, surname, username, password, email, registration_date, user_id) VALUES \
                        ('{name}', '{surname}', '{login}', '{generate_password_hash(password)}', \
                            '{email}', '{current_datetime}', '{generate_user_id()}')"
        database_query(sql_query, "none")
        return True
    except Exception as e:
        print(e)
        return False


def checking_user(login: str) -> bool:
    """Проверка на существование пользователей"""
    sql_query = f"SELECT * FROM accounts WHERE username = '{login}' AND save = true"
    cursor = database_query(sql_query, "return")
    existing_entry = cursor.fetchone()
    print(existing_entry)
    if existing_entry:
        return False    
    return True