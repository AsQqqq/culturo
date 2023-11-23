# Импорт необходимых модулей и библиотек
from culturo import login_manager
from culturo.database import db
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    "Функция для загрузки пользователя по его идентификатору"
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    "Класс, представляющий модель пользователя в базе данных"
    # Настройки таблицы в базе данных
    __table_args__ = {'schema': 'public', 'extend_existing': True}
    __tablename__ = 'accounts'

    # Поля пользователя
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)
    save = db.Column(db.Boolean, default=False)
    tested = db.Column(db.Boolean, default=False)
    common_location = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String(255), nullable=False)
