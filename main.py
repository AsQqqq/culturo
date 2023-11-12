from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Эндпоинт для получения данных из PostgreSQL
@app.route('/get_data', methods=['GET'])
def get_data():
    # Здесь выполните запрос к PostgreSQL и получите данные
    # Возвращайте данные в формате JSON
    data = fetch_data_from_postgresql()
    return jsonify(data)

# Эндпоинт для добавления новых данных
@app.route('/add_data', methods=['POST'])
def add_data():
    # Здесь обработайте новые данные и отправьте сообщение по WebSocket
    socketio.emit('update_data', namespace='/socket')
    return jsonify({'success': True})


@app.route('/confirmCard', methods=['POST'])
def confirm_swipe():
    return 'Понравилось!'


@app.route('/trashCard', methods=['POST'])
def trash_swipe():
    return 'Не понравилось!'


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("main.html")

def fetch_data_from_postgresql():
    return ['123', '321', 'saddf', 'hfgjihgdf']

if __name__ == '__main__':
    socketio.run(app, debug=True)
