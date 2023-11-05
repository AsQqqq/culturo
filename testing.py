from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MAIL_SERVER'] = 'your_mail_server'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@example.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

mail = Mail(app)

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    confirmed = fields.Boolean()

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']

        # Check if user with same username or email already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists')
            return redirect(url_for('register'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        # Send confirmation email
        token = generate_confirmation_token(new_user.email)
        confirm_url = url_for('confirm_email', token=token, _external=True)
        html = render_template('confirmation_email.html', confirm_url=confirm_url)
        subject = 'Please confirm your email'
        send_email(new_user.email, subject, html)

        flash('A confirmation email has been sent. Please check your inbox.', 'success')
        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = confirm_token(token)
    except:
        flash('The confirmation link is invalid or has expired.', 'danger')
        return redirect(url_for('home'))

    user = User.query.filter_by(email=email).first_or_404()
    if user.confirmed:
        flash('Account already confirmed. Please login.', 'success')
    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')

    return redirect(url_for('home'))

def generate_confirmation_token(email):
    # Generate token for email confirmation
    return email

def confirm_token(token, expiration=3600):
    # Check token for email confirmation
    return token

def send_email(to, subject, template):
    # Send email
    msg = Message(
            subject=subject,
            recipients=[to],
            html=template,
            sender=app.config['MAIL_USERNAME']
        )
    mail.send(msg)

if __name__ == '__main__':
    db.create_all()
    app.run()