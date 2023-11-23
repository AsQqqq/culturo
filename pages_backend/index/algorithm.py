



"""
     _    _     ____  ___ _____ ___ _____ _   _ __  __ 
    / \  | |   / ___|/ _ \_   _|_ _|_   _| | | |  \/  |
   / _ \ | |  | |  _| | | || |  | |  | | | |_| | |\/| |
  / ___ \| |__| |_| | |_| || |  | |  | | |  _  | |  | |
 /_/   \_\_____\____|\___/ |_| |___| |_| |_| |_|_|  |_|

"""


from flask import render_template, flash, jsonify, request
from pages_backend import app
from flask_login import current_user
from flask_login import current_user
from database.queries import select_user_profile, select_all_places, add_user_place, rate_place_user, select_non_liked_local, select_global_ids, \
    select_global_info, select_all_local_info, select_local_info




@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    "Работа свайпов для выявления результатов мест"
    global place_id
    try:
        if request.method == "POST":
            data_pages = request.get_json()
            if data_pages == 'confirm':
                rate_place_user(place_id=place_id, choice="confirm", username=current_user.username)
            elif data_pages == 'trash':
                rate_place_user(place_id=place_id, choice="trash", username=current_user.username)

            data = fetch_data_from_postgresql()
            if data == None:
                data = ('none_png.png', 'Пустой заголовок.', 'Попробуйте обновить страницу.')
                return jsonify(data)
            else:
                card_data = [data[0], data[1], data[2]]
                return jsonify(card_data)
        
        elif request.method == "GET":
            data = fetch_data_from_postgresql()
            if data == None:
                data = ('none_png.png', 'Пустой заголовок.', 'Попробуйте обновить страницу.')
                return jsonify(data)
            else:
                card_data = [data[0], data[1], data[2]]
                add_user_place(user_id=current_user.user_id, place_id=place_id, username=current_user.username)
                return jsonify(card_data)
    except Exception as e:
        print(e)
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')


def fetch_data_from_postgresql():
    """Алгоритм сайта"""
    global place_id
    try:
        username = current_user.username
        location = current_user.common_location

        exist = select_user_profile(username=username)
        if not exist:
            return select_recom_place(location=location)
        else:
            exist_local = select_non_liked_local(username=username)
            exist_local_all = select_all_local_info(username=username)
            exist_global = select_global_ids()
            best_point = select_max_ectimation(exist_local, exist_global, exist_local_all)
            print(f"best_point :: {best_point}")
            if best_point == None:
                place_id = None
                return None
            else:
                place_id = best_point[0][15]
                return best_point[0][2], best_point[0][1], best_point[0][3]
    except Exception as e:
        print(e)


def select_recom_place(location: str):
    global place_id
    exist = select_all_places()
    if exist:
        if count_location(exists=exist, location=location) > 2:
            for i in exist:
                if str(i[9]) == location:
                    place_id = i[15]
                    return i[2], i[1], i[3]
        else:
            if count_location(exists=exist, location=location) == 1:
                for i in exist:
                    if str(i[9]) == location:
                        place_id = i[15]
                        return i[2], i[1], i[3]
            else:
                for i in exist:
                    place_id = i[15]
                    return i[2], i[1], i[3]



def select_max_ectimation(exist_local, exist_global, exist_local_all):
    max_local = []
    max_global = []
    max_local_all = []

    for i in exist_local:
        max_local.append((i[1], i[0]))
    
    for i in exist_local_all:
        max_local_all.append((i[1], i[0]))
    
    for i in exist_global:
        max_global.append((i[0], i[1]))

    max_global = [i for i in max_global if i[1] not in [j[1] for j in max_local_all]]

    if max_global:
        best_place = max(max_global, key=lambda x: x[0])[1]
        best_place = select_global_info(place_id=best_place)
        return best_place
    else:
        if max_local:
            max_local_return = []
            max_score = None
            for i in max_local:
                selected = select_local_info(username=current_user.username, place_id=i[1])
                # print(selected)
                current_score = float(selected[5])
                current_requests = int(selected[6])
                
                if max_score is None or current_score > max_score:
                    max_score = current_score
                    max_local_return = [(selected[1], selected[5], selected[6])]
                elif current_score == max_score and current_requests < max_local_return[0][2]:
                    max_local_return = [(selected[1], selected[5], selected[6])]

            # print(max_local_return)
            
            best_place = select_global_info(place_id=max_local_return[0][0])
            return best_place
        else:
            return None

def count_location(exists, location: str):
    """Просмотр сколько значений есть для локации в выводе postgresql"""
    count = 0
    for i in exists:
        if str(i[9]) == location:
            count += 1
    return count