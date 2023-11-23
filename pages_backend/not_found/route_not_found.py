



"""
  _   _  ___ _____   _____ ___  _   _ _   _ ____  
 | \ | |/ _ \_   _| |  ___/ _ \| | | | \ | |  _ \ 
 |  \| | | | || |   | |_ | | | | | | |  \| | | | |
 | |\  | |_| || |   |  _|| |_| | |_| | |\  | |_| |
 |_| \_|\___/ |_|   |_|   \___/ \___/|_| \_|____/ 

"""

from flask import render_template, flash
from pages_backend import app


@app.errorhandler(404)
def page_not_found(e):
    """Страница не найдена"""
    try:
        return render_template('not_found.html'), 404
    except Exception as e:
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')