from flask import render_template, flash
from pages_backend import app


@app.errorhandler(404)
def page_not_found(e):
    try:
        return render_template('not_found.html'), 404
    except Exception as e:
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')