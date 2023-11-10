from flask import render_template
from pages_backend import app
from flask_login import current_user


@app.route('/', methods=['GET'])
def index() -> render_template:
    """Основная вкладка"""
    if current_user.is_authenticated:
        return render_template('validation_code.html')
    else:
        return render_template('index.html')

def upload_index():
    return True