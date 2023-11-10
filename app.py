from pages_backend.reg import (
    route_index,
    route_register,
    route_login,
    logout_login,
    route_not_found
)
from register import app, login_manager
from database.sqlAlchemy import User


host = "192.168.0.104"
port = 5500
domain = f"http://{host}:{port}"

@app.before_request
def before_request():
    print("Пре запрос")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    "Запуск кода"
    # generate_verification_code(login="asq")
    # app.run(debug=True, host=host, port=port, ssl_context='adhoc')
    app.run(debug=True, host=host, port=port)