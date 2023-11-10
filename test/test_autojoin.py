from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на свой секретный ключ
csrf = CSRFProtect(app)

login_manager = LoginManager()
login_manager.init_app(app)

# Пример модели пользователя
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# Пример базы данных пользователей
users = {'user1': {'password': 'password1'}}

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Форма входа
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# Представление для входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if users.get(username) and users[username]['password'] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html', form=form)

# Представление для выхода
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Защищенное представление
@app.route('/')
@login_required
def index():
    return 'Hello, you are logged in!'

if __name__ == '__main__':
    app.run(debug=True)