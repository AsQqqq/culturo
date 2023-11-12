from flask import render_template, flash, jsonify, request
from pages_backend import app
from flask_login import current_user
import main_index
from database import get_data_database_testing
from database.decorators import get_testing



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
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')




@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    if request.method == "POST":
        data_pages = request.get_json()
        data = fetch_data_from_postgresql()
        if data_pages == 'confirm':
            result = "confirm_result"
        elif data_pages == 'trash':
            # Обработка данных для 'trash'
            result = "trash_result"
        else:   
            # Обработка других случаев
            result = "ERROR"
        print(f"\n\n{result}\n\n")
        return jsonify(data)
    elif request.method == "GET":
        data = fetch_data_from_postgresql()
        return jsonify(data)

def fetch_data_from_postgresql():
    return ['123', '321', 'saddf', 'hfgjihgdf']







def upload_index():
    return True