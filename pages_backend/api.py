from .index.database_route import get_all_place_api, generate_api, check_validate_token, active_token, active_token_api
from flask import render_template, jsonify, redirect, url_for, flash
from pages_backend import app
from flask_login import current_user
from database.decorators import get_testing

@app.route('/api/<token>')
def api(token):
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
    try:
        if get_testing(user_id=current_user.user_id):
            if active_token_api(username=current_user.username):
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
    return active_token(username=current_user.username)


def upload_api():
    return True