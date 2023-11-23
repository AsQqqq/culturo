



"""
  ____  _____ _____ _____ ___ _   _  ____    _____ _        _    ____  _  __
 / ___|| ____|_   _|_   _|_ _| \ | |/ ___|  |  ___| |      / \  / ___|| |/ /
 \___ \|  _|   | |   | |  | ||  \| | |  _   | |_  | |     / _ \ \___ \| ' / 
  ___) | |___  | |   | |  | || |\  | |_| |  |  _| | |___ / ___ \ ___) | . \ 
 |____/|_____| |_|   |_| |___|_| \_|\____|  |_|   |_____/_/   \_\____/|_|\_\

"""                                       

# Импорт необходимых модулей Flask
from flask import Flask
from flask_login import LoginManager
from decoding import get_config_server

# Создание экземпляра Flask приложения
app = Flask(__name__)
app.secret_key = '-LZwbN4Bo-'  # Установка секретного ключа для обеспечения безопасности

# Инициализация LoginManager для управления аутентификацией пользователей
login_manager = LoginManager()
login_manager.init_app(app)

# Конфигурация для сайта (домен)
host = get_config_server()[0]
port = get_config_server()[1]
domain = f"http://{host}:{port}"
print(domain)

# Конфигурация Flask приложения
app.config['JSON_AS_ASCII'] = False  # Установка кодировки для корректного отображения не ASCII символов
login_manager.login_view = 'index'  # Установка представления для входа в систему