from flask import render_template
from pages_backend import app

@app.route('/login', methods=['GET'])
def login() -> str: 
    "О нас"
    return render_template('sign_in.html')

def upload_login():
    return True