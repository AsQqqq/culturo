



"""
  _____ _____ ____ _____ _____ ____  
 |_   _| ____/ ___|_   _| ____|  _ \ 
   | | |  _| \___ \ | | |  _| | | | |
   | | | |___ ___) || | | |___| |_| |
   |_| |_____|____/ |_| |_____|____/ 

"""

from flask import redirect, url_for, request, flash, render_template
from pages_backend import app
from flask_login import current_user
from config import link_index
from database.queries import user_testing_changed, add_common_location_from_test


@app.route('/process_form', methods=['POST'])
def process_form():
    try:
        if current_user.is_authenticated:
            selected_place = request.form.get('selected_location')
            if str(selected_place) != "None":
                if str(selected_place).replace(" ", "") != "":
                    user_id = current_user.user_id
                    user_testing_changed(user_id=user_id)
                    add_common_location_from_test(user_id=user_id, location=selected_place)
                    return redirect(url_for(link_index))
                flash("Укажите свои предпочтения", "error")
                return redirect(url_for(link_index))
            else:
                flash("Укажите свои предпочтения", "error")
                return redirect(url_for(link_index))
    except Exception as e:
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        print(e)
        return render_template('sign_in.html')


def upload_index():
    return True