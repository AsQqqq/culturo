from flask import render_template, flash
from pages_backend import app
from database.queries import select_all_places


@app.route('/hello', methods=['GET'])
def page_not_found():
    """Страница не найдена"""
    try:
        return str(select_all_places())
    except Exception as e:
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('index.html')