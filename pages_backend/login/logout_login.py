from pages_backend import app
from flask import redirect, url_for
from flask_login import login_required, logout_user


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))