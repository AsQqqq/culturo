from flask import render_template, flash, url_for, redirect
from pages_backend import app
from flask_login import current_user
import main_index
from database.decorators import get_testing
from flask_login import current_user
from . import database_places


@app.route('/places', methods=['GET', 'POST'])
def places() -> render_template:
    try:
        if current_user.is_authenticated:
            user_id = current_user.user_id
            if get_testing(user_id=user_id):
                database_place = database_places.get_all_locale_true_places(username=current_user.username)
                if database_place == False:
                    return "Пусто"
                else:
                    id_point = []
                    position_info = []
                    text = "Нет информации"
                    for i in database_place:
                        id_point.append(i[1])                        

                    for i in id_point:
                        result = database_places.get_info_position(ip_point=i)
                        
                        for n in result:
                            hours_of_operation_start = text if n[3] == "" else n[3]
                            hours_of_operation_end = text if n[4] == "" else n[4]
                            contact_phone = text if n[5] == "" else n[5]
                            email = text if n[6] == "" else n[6]
                            date_open = text if n[7] == "" else n[7]
                            site = text if n[9] == "" else n[9]
                            break_time_start = text if n[10] == "" else n[10]
                            break_time_end = text if n[11] == "" else n[11]
                            
                            position_info.append((n[1], n[0], n[2], n[8], i, hours_of_operation_start, hours_of_operation_end, contact_phone, email, date_open, site, break_time_start, break_time_end))
                        break

                    print(position_info)
                    return position_info
                # return render_template("profile.html", username=current_user.name, token=check_active_token())
            else:
                return redirect(url_for(main_index.testing))
        else:
            return redirect(url_for(main_index.testing))
    except Exception as e:
        print(e)
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')


def upload_places():
    return True