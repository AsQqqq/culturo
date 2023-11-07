from flask import render_template, request, redirect, url_for, flash
from flask_mail import Message
from pages_backend import app
from . import selected_verification_code, checking_user, \
    pre_save_account, generate_verification_code, mail



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
            flash("Такой пользователь уже существует. Пожалуйста, проверьте введенные данные и попробуйте снова.", "error")
            return render_template('sign_up.html')
        else:
            if password == confirm_password:
                if len(name) > 2 and len(surname) > 2 and len(email) > 2 and len(login) > 2 and len(password) and len(confirm_password) > 2:
                    generate_verification_code(login=login)
                    verification_code = selected_verification_code(login=login)

                    message_body = render_template('email_confirmation.html', token=verification_code)

                    if pre_save_account(name=name,
                                     surname=surname,
                                     email=email,
                                     login=login,
                                     password=password):
                        # Отправка письма
                        msg = Message('Подтверждение электронной почты', sender=f"my-email@gmail.com", recipients=[email])
                        msg.html = message_body
                        mail.send(msg)

                        return redirect(url_for('validation_code', email=email))
                    flash("Ошибка сервера.", "error")
                    try:
                        return redirect(url_for('sign_up'))
                    except:
                        return render_template('sign_up.html')
                else:
                    flash("Введенные данные не прошли валидацию. Пожалуйста, проверьте введенные данные и попробуйте снова.", "error")
                    try:
                        return redirect(url_for('sign_up'))
                    except:
                        return render_template('sign_up.html')
            else:
                flash("Пароли не совпадают. Пожалуйста, проверьте введенные данные и попробуйте снова.", "error")
                try:
                    return redirect(url_for('sign_up'))
                except:
                    return render_template('sign_up.html')
    elif request.method == "GET":
        return render_template('sign_up.html')
    
def upload_register():
    return True