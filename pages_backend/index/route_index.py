from flask import render_template, Blueprint
from pages_backend import app

simple_page = Blueprint('index', __name__, template_folder='templates')
@app.route('/', methods=['GET'])
def index() -> render_template:
    """Основная вкладка"""
    return render_template('index.html')

def upload_index():
    return True