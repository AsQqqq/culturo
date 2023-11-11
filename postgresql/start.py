import subprocess
import os

os.environ['PGUSER'] = 'postgres'
os.environ['PGPASSWORD'] = 'root'
os.environ['PGHOST'] = 'localhost'
path = "postgresql/"


def index():
    print("1 - config.sql")
    print("2 - delete_config.sql")
    choice = input("1/2 ----> ")
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

if __name__ == "__main__":
    index()