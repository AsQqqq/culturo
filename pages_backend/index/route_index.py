from flask import render_template, flash, jsonify, request
from pages_backend import app
from flask_login import current_user
import main_index
from database import get_data_database_testing
from database.decorators import get_testing
from flask_login import current_user

from .database_route import select_all_user, select_all_place, add_user_place, confirm_trash_place_user


place_id = "None"


@app.route('/', methods=['GET'])
def index() -> render_template:
    """Основная вкладка"""
    try:
        if current_user.is_authenticated:
            user_id = current_user.user_id
            if get_testing(user_id=user_id):
                return render_template("main.html")
            else:
                items = set(get_data_database_testing())
                return render_template(f"{main_index.index}.html", items=items)
        else:
            return render_template('index.html')
    except Exception as e:
        print(e)
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')



@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    global place_id
    try:
        if request.method == "POST":
            data_pages = request.get_json()
            data = fetch_data_from_postgresql()

            if data_pages == 'confirm':
                confirm_trash_place_user(place_id=place_id, choice="confirm", username=current_user.username)
            elif data_pages == 'trash':
                confirm_trash_place_user(place_id=place_id, choice="trash", username=current_user.username)

            card_data = [data[0], data[1], data[2]]
            return jsonify(card_data)
        
        elif request.method == "GET":
            data = fetch_data_from_postgresql()
            card_data = [data[0], data[1], data[2]]
            add_user_place(user_id=current_user.user_id, place_id=place_id, username=current_user.username)
            return jsonify(card_data)
    except Exception as e:
        print(e)
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')


def fetch_data_from_postgresql():
    """Алгоритм сайта"""
    global place_id
    try:
        username = current_user.username
        location = current_user.common_location

        exist = select_all_user(username=username)
        if not exist:
            exist = select_all_place()
            if exist:
                if count_location(exists=exist, location=location) > 2:
                    for i in exist:
                        if str(i[9]) == location:
                            place_id = i[15]
                            return i[2], i[1], i[3]
                else:
                    if count_location(exists=exist, location=location) == 1:
                        for i in exist:
                            if str(i[9]) == location:
                                place_id = i[15]
                                return i[2], i[1], i[3]
                    else:
                        for i in exist:
                            place_id = i[15]
                            return i[2], i[1], i[3]
        else:
            pass
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')
    except Exception as e:
        print(e)
    


def count_location(exists, location: str):
    """Просмотр сколько значений есть для локации в выводе postgresql"""
    count = 0
    for i in exists:
        if str(i[9]) == location:
            count += 1
    return count




def upload_index():
    return True