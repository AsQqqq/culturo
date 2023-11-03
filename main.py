from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index() -> render_template:
    """Основная вкладка"""
    return render_template('index.html')
    return "Main Page"


@app.route('/login')
def login() -> str: 
    "О нас"
    return render_template('sign_in.html')


@app.route('/register')
def register() -> str: 
    "О нас"
    return render_template('sign_up.html')

if __name__ == "__main__":
    "Запуск кода"
    app.run(debug=True, host="127.0.0.1", port=5500)