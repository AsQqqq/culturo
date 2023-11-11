from database.dibs import database_query
from datetime import datetime
from . import generate_code, generate_user_id
from werkzeug.security import generate_password_hash



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


def generate_verification_code(login: str):
    """Генерация проверочного кода"""
    code = generate_code(login=login)

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