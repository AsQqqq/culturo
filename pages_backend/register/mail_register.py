from flask import render_template, request, redirect, url_for, flash
from flask_mail import Mail
from database.queries import code_search_in_the_database, account_confirmation
from pages_backend import app
from flask_login import current_user
from config import link_testing

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
    try:
        if current_user.is_authenticated:
            return redirect(url_for("index"))
        
        if code_search_in_the_database(code=code):
            account_confirmation(code=code)
            return redirect(url_for(("login")))
        return redirect(url_for('index'))
    except Exception as e:
        print(e)
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')


@app.route('/validation_code/<email>')
def validation_code(email) -> str: 
    try:
        if current_user.is_authenticated:
            return redirect(url_for((link_testing)))
        
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
    except Exception as e:
        print(e)
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')