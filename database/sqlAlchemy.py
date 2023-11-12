from register import db, login_manager
from sqlalchemy import types
from flask_login import UserMixin


class Point(types.TypeDecorator):
    impl = types.String

    def process_bind_param(self, value, dialect):
        if value is not None:
            return f'({value[0]}, {value[1]})'

    def process_result_value(self, value, dialect):
        if value is not None:
            return tuple(map(float, value[1:-1].split(', ')))



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __table_args__ = {'schema': 'public', 'extend_existing': True}
    __tablename__ = 'accounts'

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