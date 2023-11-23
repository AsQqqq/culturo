



"""
  ____    _  _____  _    ____    _    ____  _____    ____  _____ _____ _____ ___ _   _  ____ 
 |  _ \  / \|_   _|/ \  | __ )  / \  / ___|| ____|  / ___|| ____|_   _|_   _|_ _| \ | |/ ___|
 | | | |/ _ \ | | / _ \ |  _ \ / _ \ \___ \|  _|    \___ \|  _|   | |   | |  | ||  \| | |  _ 
 | |_| / ___ \| |/ ___ \| |_) / ___ \ ___) | |___    ___) | |___  | |   | |  | || |\  | |_| |
 |____/_/   \_\_/_/   \_\____/_/   \_\____/|_____|  |____/|_____| |_|   |_| |___|_| \_|\____|

"""                                                  

# Импорт экземпляра Flask приложения
from culturo import app
from decoding import get_database_config_main
from flask_sqlalchemy import SQLAlchemy

# Получение данных из зашифрованного файла
login_base = get_database_config_main()[0]
login_password = get_database_config_main()[4]
ip_base = get_database_config_main()[1]
base_password = get_database_config_main()[2]

# Настройка параметров подключения к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{login_base}:{base_password}@{ip_base}/{login_password}'

# Создание объекта SQLAlchemy для взаимодействия с базой данных
db = SQLAlchemy(app)
