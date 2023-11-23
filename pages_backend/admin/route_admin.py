from flask import render_template, jsonify, redirect, url_for
from flask_login import current_user
from .database_admin import count_all_accounts, count_all_places
from pages_backend import app

active_users = 0


@app.route('/admin')
def counter():
    if current_user.is_authenticated and (current_user.username == "danila" or current_user.username == "serafim"): 
        return render_template("stat.html")
    else:
        return render_template('not_found.html'), 404


@app.route('/statistic', methods=["GET"])
def statistic():
    if current_user.is_authenticated and (current_user.username == "danila" or current_user.username == "serafim"):
        total_accounts = count_all_accounts()
        total_places = count_all_places()
        return jsonify(total_accounts=total_accounts, total_places=total_places)
    else:
        return render_template('not_found.html'), 404

def upload_admin():
    return True