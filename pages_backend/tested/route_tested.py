from flask import redirect, url_for, request, flash, render_template
from pages_backend import app
from flask_login import current_user
import main_index



@app.route('/process_form', methods=['POST'])
def process_form():
    try:
        if current_user.is_authenticated:
            selected_place = request.form.get('selected_location')
            if str(selected_place) != "None":
                return f'{selected_place}'
            else:
                flash("Укажите свои предпочтения", "error")
                return redirect(url_for(main_index.testing))
    except Exception as e:
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')


def upload_index():
    return True