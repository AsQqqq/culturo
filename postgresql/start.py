import subprocess
import os

os.environ['PGUSER'] = 'postgres'
os.environ['PGPASSWORD'] = 'root'

path = "postgresql/"
config_file = "config.sql"

command = f"psql -f {path}{config_file}"
process = subprocess.Popen(command, shell=True)
process.wait()