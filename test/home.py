from flask import Flask, render_template, redirect, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')

@socketio.on('message')
def handle_message(data):
    message = data['message']
    if message != "root":
        emit('notification', {'message': 'Уведомление: ' + message}, broadcast=True)
    else:
        emit('redirect', {'url': '/sign_in'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)