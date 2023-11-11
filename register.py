from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from decoding import get_database_place


ip_base = get_database_place()[1]
login_base = get_database_place()[0]
password_base = get_database_place()[2]
password_name = get_database_place()[4]

app = Flask(__name__)
app.secret_key = 'culturo31passwordSecretKey'
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'index'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{login_base}:{password_base}@{ip_base}/{password_name}'
print(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)