from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
socketio = SocketIO(app)

active_users = 0

@app.route('/')
def index():
    return render_template('index.html', active_users=active_users)

@socketio.on('connect')
def handle_connect():
    global active_users
    active_users += 1
    emit('update_users', {'active_users': active_users}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    global active_users
    active_users -= 1
    emit('update_users', {'active_users': active_users}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
