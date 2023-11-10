from flask import render_template
from register import app


@app.errorhandler(404)
def page_not_found(e):
    return render_template('not_found.html'), 404