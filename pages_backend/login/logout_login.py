from pages_backend import app
from flask import redirect, url_for, flash, render_template
from flask_login import login_required, logout_user, current_user
from register import login_manager
from time import sleep



@app.route('/logout', methods=['GET'])
@login_required
@login_manager.unauthorized_handler
def unauthorized_callback():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
