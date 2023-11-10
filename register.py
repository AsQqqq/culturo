from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://culturopro:EptGvfiHh1KVkpKS-Qkn@localhost/culturo'
db = SQLAlchemy(app)