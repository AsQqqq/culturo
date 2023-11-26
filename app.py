



"""
  ____ _____  _    ____ _____    _____ _        _    ____  _  __
 / ___|_   _|/ \  |  _ \_   _|  |  ___| |      / \  / ___|| |/ /
 \___ \ | | / _ \ | |_) || |    | |_  | |     / _ \ \___ \| ' / 
  ___) || |/ ___ \|  _ < | |    |  _| | |___ / ___ \ ___) | . \ 
 |____/ |_/_/   \_\_| \_\|_|    |_|   |_____/_/   \_\____/|_|\_\

"""

# Импорт экземпляра Flask приложения app, хоста и порта
from culturo import app, host, port
from pages_backend.reg import route


# Запуск Flask приложения, отключение режима отладки и указание хоста и порта
if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)