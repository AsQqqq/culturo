from database.dibs import database_query
import secrets


def selected_verification_code(login: str) -> str:
    """Чтение проверочного кода"""
    sql_query = f"SELECT * FROM code WHERE login = '{login}'"
    cursor = database_query(sql_query, "place", "return")
    existing_entry = cursor.fetchone()
    return str(existing_entry[1])


def generate_code(login: str):
    code = f"{secrets.token_hex(16)}-{secrets.token_hex(16)}-{secrets.token_hex(16)}-{login}"
    return code


def generate_user_id():
    code = f"{secrets.token_hex(16)}"
    copy_query = f"SELECT * FROM accounts WHERE user_id = '{code}'"
    cursor = database_query(copy_query, "place", "return")
    existing_entry = cursor.fetchone()

    if existing_entry:
        generate_user_id()
        return

    return code