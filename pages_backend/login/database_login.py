from database.dibs import database_query
from werkzeug.security import check_password_hash



def checking_user(login: str, password: str) -> bool:
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
    
    print(existing_entry)

    return True