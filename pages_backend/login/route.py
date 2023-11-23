



"""
  _     ___   ____ ___ _   _ 
 | |   / _ \ / ___|_ _| \ | |
 | |  | | | | |  _ | ||  \| |
 | |__| |_| | |_| || || |\  |
 |_____\___/ \____|___|_| \_|

"""


from flask import render_template, request, flash, redirect, url_for
from pages_backend import app
from database.user_model import User
from flask_login import login_user
from flask_login import current_user
from config import link_index
from database.queries import check_exist_in_database_user


@app.route('/login', methods=['GET', 'POST'])
def login() -> str: 
    "Страница входа пользователя"
    try:
        if current_user.is_authenticated:
            return redirect(url_for((link_index)))
        if request.method == "POST":
            login = request.form.get('login')
            password = request.form.get('password')
            if check_exist_in_database_user(login=login, password=password) == False:
                flash("Такого пользователя не существует. Пожалуйста, проверьте введенные данные и попробуйте снова.", "error")
                return render_template('sign_in.html')

            user = User.query.filter_by(username=login).first()
            login_user(user)
            return redirect(url_for((link_index)))
        
        elif request.method == "GET":
            return render_template('sign_in.html')
    except Exception as e:
        flash(f"Произошла внутренняя ошибка сервера. Обратитесь к администратору. {e}", "error")
        return render_template('sign_in.html')
        

def upload_login():
    return True