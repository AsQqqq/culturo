from flask import redirect, url_for, request, flash, render_template
from pages_backend import app
from flask_login import current_user
import main_index
from database.decorators import replace_tested_changed, replace_add_tested_location



@app.route('/process_form', methods=['POST'])
def process_form():
    try:
        if current_user.is_authenticated:
            selected_place = request.form.get('selected_location')
            if str(selected_place) != "None":
                if str(selected_place).replace(" ", "") != "":
                    user_id = current_user.user_id
                    replace_tested_changed(user_id=user_id)
                    replace_add_tested_location(user_id=user_id, location=selected_place)
                    return redirect(url_for(main_index.testing))
                flash("Укажите свои предпочтения", "error")
                return redirect(url_for(main_index.testing))
            else:
                flash("Укажите свои предпочтения", "error")
                return redirect(url_for(main_index.testing))
    except Exception as e:
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        print(e)
        return render_template('sign_in.html')


def upload_index():
    return True