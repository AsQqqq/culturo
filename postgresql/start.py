



"""
  ____   ___  _        ____ ___  _   _ _____ ___ ____ 
 / ___| / _ \| |      / ___/ _ \| \ | |  ___|_ _/ ___|
 \___ \| | | | |     | |  | | | |  \| | |_   | | |  _ 
  ___) | |_| | |___  | |__| |_| | |\  |  _|  | | |_| |
 |____/ \__\_\_____|  \____\___/|_| \_|_|   |___\____|

"""

# Импорт необходимых модулей
import subprocess
import os

# Установка переменных среды для PostgreSQL
os.environ['PGUSER'] = 'postgres'
os.environ['PGPASSWORD'] = 'root'
os.environ['PGHOST'] = 'localhost'

# Определение пути для SQL-файлов
path = "postgresql/"

# Функция для выполнения действий в зависимости от выбора пользователя
def index():
    # Вывод пользователю доступных опций
    print("1 - config.sql")
    print("2 - delete_config.sql")

    # Получение выбора пользователя
    choice = input("1/2 ----> ")

    # Выполнение SQL-файла в зависимости от выбора пользователя
    if choice == "1":
        config_file = "config.sql"

        command = f"psql -h localhost -f {path}{config_file}"
        process = subprocess.Popen(command, shell=True)
        process.wait()
    elif choice == "2":
        config_file = "delete_config.sql"

        command = f"psql -h localhost -f {path}{config_file}"
        process = subprocess.Popen(command, shell=True)
        process.wait()
    else:
        index()

# Запуск функции index(), если скрипт выполняется как основной
if __name__ == "__main__":
    index()
