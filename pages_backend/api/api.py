



"""
     _    ____ ___ 
    / \  |  _ \_ _|
   / _ \ | |_) | | 
  / ___ \|  __/| | 
 /_/   \_\_|  |___|

"""

from database.queries import get_all_place_api, generate_api, check_validate_token, select_user_token, check_exist_token, get_testing
from flask import render_template, jsonify, redirect, url_for, flash, send_file
from pages_backend import app
from flask_login import current_user



@app.route('/api/<token>')
def api(token):
    """Обработка запроса по ключу API"""
    try:
        if check_validate_token(token=token) == True:
            cursor = get_all_place_api()
            data = [{"id": row[0], "name": row[1], "location": row[2]} for row in cursor]
            # return data
            return jsonify(data), 200, {'Content-Type': 'application/json; charset=latina'}
        else:
            return render_template('not_found.html'), 404
    except Exception as e:
        print(e)
        return render_template('not_found.html'), 404


@app.route('/generate_api_key')
def generate_api_key():
    """Генерация API ключа"""
    try:
        if get_testing(user_id=current_user.user_id):
            if check_exist_token(username=current_user.username):
                flash("Токен уже сгенерирован")
                return redirect(url_for("profile"))
            else:
                generate_api(username=current_user.username)
                return redirect(url_for("profile"))
        else:
            return render_template('not_found.html'), 404
    except Exception as e:
        print(e)
        return render_template('not_found.html'), 404


def check_active_token():
    "Проверка токена на эксплюзивность"
    return select_user_token(username=current_user.username)


def upload_api():
    return True