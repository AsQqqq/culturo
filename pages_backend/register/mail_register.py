from flask import render_template, request, redirect, url_for
from flask_mail import Mail
from database.dibs import database_query
from pages_backend import app


mail = 'culturo31@gmail.com'
password_mail = 'yxfv xizy rmte xvtq'


# Настройки для подключения к серверу почты
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = mail
app.config['MAIL_PASSWORD'] = password_mail
mail = Mail(app)


@app.route('/confirm_email/<code>')
def confirm_email(code):
    sql_query = f"SELECT * FROM code WHERE code = '{code}'"
    cursor = database_query(sql_query, "place", "return")
    existing_entry = cursor.fetchone()
    if existing_entry:
        sql_query = f"UPDATE code SET activate = False WHERE code = '{code}'"
        cursor = database_query(sql_query, "place", "none")

        code_nickname = code.split("-")[3]
        sql_query = f"UPDATE accounts SET save = True WHERE username = '{code_nickname}'"
        cursor = database_query(sql_query, "place", "none")
        return redirect(url_for("index"))
    return redirect(url_for('not_found'))


@app.route('/validation_code/<email>')
def validation_code(email) -> str: 
    domain = email.split("@")[-1].lower()
    if domain == "yandex.ru":
        email_url = "https://mail.yandex.ru"
    elif domain == "gmail.com":
        email_url = "https://mail.google.com"
    else:
        email_url = f"https://mail.{domain}"

    if request.method == "POST":
        return render_template('validation_code.html', email=email_url)
    else:
        return render_template('validation_code.html', email=email_url)