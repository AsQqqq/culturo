from pages_backend.reg import (
    route_index
)
from register import app, login_manager
from database.sqlAlchemy import User
from decoding import get_ipport


host = get_ipport()[0]
port = get_ipport()[1]
domain = f"http://{host}:{port}"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    "Запуск кода"
    app.run(debug=False, host=host, port=port)