from pages_backend.reg import (
    route_index,
    route_register,
    route_login
)
from register import app


host = "127.0.0.1"
port = 5500


domain = f"http://{host}:{port}"

# @app.before_request
# def before_request():
#     print("Пре запрос")

if __name__ == "__main__":
    "Запуск кода"
    # generate_verification_code(login="asq")
    app.run(debug=True, host=host, port=port)