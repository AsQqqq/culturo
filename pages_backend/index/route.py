



"""
  ____   ___  _   _ _____ _____    ___ _   _ ____  _______  __
 |  _ \ / _ \| | | |_   _| ____|  |_ _| \ | |  _ \| ____\ \/ /
 | |_) | | | | | | | | | |  _|     | ||  \| | | | |  _|  \  / 
 |  _ <| |_| | |_| | | | | |___    | || |\  | |_| | |___ /  \ 
 |_| \_\\___/ \___/  |_| |_____|  |___|_| \_|____/|_____/_/\_\

"""


from flask import render_template, flash
from pages_backend import app
from flask_login import current_user
from config import link_testing
from database import get_common_location_from_test
from database.queries import get_testing


place_id = "None"


@app.route('/', methods=['GET'])
def index() -> render_template:
    """Основная функция прогрузки страницы"""
    try:
        if current_user.is_authenticated:
            user_id = current_user.user_id
            if get_testing(user_id=user_id):
                return render_template("main.html", username=current_user.name)
            else:
                items = set(get_common_location_from_test())
                return render_template(f"{link_testing}.html", username=current_user.name, items=items)
        else:
            return render_template('index.html')
    except Exception as e:
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('index.html')


def upload_index():
    return True