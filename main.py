from flask import Flask, render_template, request, redirect, url_for
from database import dibs
import secrets
from flask_mail import Mail, Message

app = Flask(__name__)

host = "127.0.0.1"
port = 5500

domain = f"http://{host}:{port}"

mail = 'danila.udodov.workmail@gmail.com'
password_mail = 'rleu hrbi vtav dlsv'

# Настройки для подключения к серверу почты
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail
app.config['MAIL_PASSWORD'] = password_mail
mail = Mail(app)


@app.before_request
def before_request():
    print("Пре запрос")


@app.route('/', methods=['GET'])
def index() -> render_template:
    """Основная вкладка"""
    return render_template('index.html')


@app.route('/login', methods=['GET'])
def login() -> str: 
    "О нас"
    return render_template('sign_in.html')


@app.route('/register', methods=['POST', 'GET'])
def register() -> str: 
    if request.method == "POST":
        name = request.form.get('name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        login = request.form.get('login')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not checking_user(login=login):
            # Здесь уведомление!!!
            pass
        else:
            if password == confirm_password:
                if len(name) > 2 and len(surname) > 2 and len(email) > 2 and len(login) > 2 and len(password) and len(confirm_password) > 2:
                    generate_verification_code(login=login)
                    verification_code = selected_verification_code(login=login)

                    message_body = render_template('email_confirmation.html', token=verification_code)

                    # Отправка письма
                    msg = Message('Подтверждение электронной почты', sender=f"my-email@gmail.com", recipients=[email])
                    msg.html = message_body
                    mail.send(msg)
                    return "Вам отправлено письмо!"
                else:
                    # Здесь уведомление!!!
                    pass
            else:
                # Здесь уведомление!!!
                pass

        return redirect(url_for('login'))
    elif request.method == "GET":
        return render_template('sign_up.html')



@app.route('/confirm_email/<code>')
def confirm_email(code):
    sql_query = f"SELECT * FROM code WHERE code = '{code}'"
    cursor = database_query(sql_query, "place", "return")
    existing_entry = cursor.fetchone()
    if existing_entry:
        sql_query = f"DELETE FROM code WHERE code = '{code}'"
        cursor = database_query(sql_query, "place", "none")
        return "Код есть! Вы зареганы!"
    return "Пошёл от сюда вон!"


def selected_verification_code(login: str) -> str:
    """Чтение проверочного кода"""
    sql_query = f"SELECT * FROM code WHERE login = '{login}'"
    cursor = database_query(sql_query, "place", "return")
    existing_entry = cursor.fetchone()
    return str(existing_entry[1])


def generate_code(login: str):
    code = f"{secrets.token_hex(16)}-{secrets.token_hex(16)}-{secrets.token_hex(16)}-{login}"
    return code


def checking_user(login: str) -> bool:
    """Проверка на существование пользователей"""
    sql_query = f"SELECT * FROM accounts WHERE username = '{login}'"
    cursor = database_query(sql_query, "place", "return")
    existing_entry = cursor.fetchone()
    print(existing_entry)
    if existing_entry:
        return False    
    return True



def generate_verification_code(login: str):
    """Генерация проверочного кода"""
    code = generate_code(login=login)

    copy_query = f"SELECT * FROM code WHERE code = '{code}'"
    cursor = database_query(copy_query, "place", "return")
    existing_entry = cursor.fetchone()
    print(existing_entry)
    if existing_entry:
        generate_verification_code(login=login)
        return

    sql_query = f"SELECT * FROM code WHERE login = '{login}'"
    cursor = database_query(sql_query, "place", "return")
    existing_entry = cursor.fetchone()

    if existing_entry: 
        # Если запись существует, удалим ее
        delete_query = f"DELETE FROM code WHERE login = '{login}'"
        database_query(delete_query, "place", "none")

    sql_query = f"INSERT INTO code (code, login, activate) VALUES ('{code}', '{login}', True)"
    database_query(sql_query, "place", "none")
    
    

def database_query(sql_query: str, users: str, types: str):
    """Функция для запросов в базу данных"""
    if users == "place":
        connection, cursor = dibs.connected_database_place()
    else:
        connection, cursor = dibs.connected_database_main()

    cursor.execute(sql_query)
    
    if types == "return":
        return cursor
    
    dibs.closing_database(cursor=cursor, connection=connection)
        




if __name__ == "__main__":
    "Запуск кода"
    # generate_verification_code(login="asq")
    # selected_verification_code(login="asq")
    app.run(debug=True, host=host, port=port)