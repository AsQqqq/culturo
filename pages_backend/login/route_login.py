from flask import render_template, request, flash, redirect, url_for
from pages_backend import app
from .database_login import checking_user
from database.sqlAlchemy import User
from flask_login import login_user
from flask_login import current_user
import main_index



@app.route('/login', methods=['GET', 'POST'])
def login() -> str: 
    try:
        if current_user.is_authenticated:
            return redirect(url_for((main_index.testing)))
        
        if request.method == "POST":
            login = request.form.get('login')
            password = request.form.get('password')

            if checking_user(login=login, password=password) == False:
                flash("Такого пользователя не существует. Пожалуйста, проверьте введенные данные и попробуйте снова.", "error")
                return render_template('sign_in.html')


            user = User.query.filter_by(username=login).first()
            login_user(user)
            return redirect(url_for((main_index.testing)))
        
        elif request.method == "GET":
            return render_template('sign_in.html')
    except Exception as e:
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')
        

def upload_login():
    return True