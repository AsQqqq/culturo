from flask import render_template, flash, jsonify, request
from pages_backend import app



@app.route('/', methods=['GET'])
def index() -> render_template:
    return render_template('test.html')

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
