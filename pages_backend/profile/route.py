from flask import render_template, flash, url_for, redirect
from pages_backend import app
from flask_login import current_user
from config import link_index
from database.queries import get_testing
from flask_login import current_user
from pages_backend.api import api


@app.route('/profile', methods=['GET'])
def profile() -> render_template:
    """Профиль пользователя"""
    try:
        if current_user.is_authenticated:
            user_id = current_user.user_id
            if get_testing(user_id=user_id):
                return render_template("profile.html", username=current_user.name, token=api.check_active_token())
            else:
                return redirect(url_for(link_index))
        else:
            return redirect(url_for(link_index))
    except Exception as e:
        print(e)
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')


def upload_profile():
    return True