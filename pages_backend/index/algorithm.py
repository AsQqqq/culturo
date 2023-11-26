



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
from database.queries import (select_all_places, add_new_places, rate_place_user, 
    select_all_my_recommendation, exist_recommendation, select_places_statistics, 
    select_common_location_with_place_id, select_info_with_place_id, rate_place_user, 
    select_all_my_recommendationTRUE)


place_id = "None"


@app.route('/get_data', methods=['GET', 'POST'])
def get_data():
    "Работа свайпов для выявления результатов мест"
    global place_id
    try:
        add_user_place()
        if request.method == "POST":
            data_pages = request.get_json()
            if data_pages == 'confirm':
                rate_place_user(place_id=place_id, choice="confirm", username=current_user.username)
            elif data_pages == 'trash':
                rate_place_user(place_id=place_id, choice="trash", username=current_user.username)

            data = alhorithm_site()
            print(data)
            card_data = [data[0], data[1], data[2]]
            print(jsonify(card_data))
            return jsonify(card_data)
        
        elif request.method == "GET":
            data = alhorithm_site()
            print(data)
            card_data = [data[0], data[1], data[2]]
            print(jsonify(card_data))
            return jsonify(card_data)
    except Exception as e:
        flash("Произошла внутренняя ошибка сервера. Обратитесь к администратору.", "error")
        return render_template('sign_in.html')


def add_user_place():
    "Запись новой карточки если её нет"
    all_places = select_all_places()
    if all_places:
        for i in all_places:
            if exist_recommendation(place_id=i[0], username=current_user.username) == False:
                add_new_places(user_id=current_user.user_id, place_id=i, username=current_user.username)


def alhorithm_site():
    """Алгоритм сайта"""
    global place_id
    try:
        all_common_location = select_all_my_recommendation(username=current_user.username)
        all_places = select_all_my_recommendationTRUE(username=current_user.username)
        id_places_main = []
        statistic_integration = []
        best_places = []

        print(len(all_common_location))
        print(all_common_location)

        if len(all_common_location) >= 3:
            for i in all_common_location:
                id_places_main.append(i[0])
        else:
            for i in all_places:
                id_places_main.append(i[0])


        for i in id_places_main:
            result = select_places_statistics(place_id=i, username=current_user.username)
            list_ = [i, result[0][0], result[0][1]]
            statistic_integration.append(list_)

        print("LOGIC----------------")
        for _ in range(0, 3):
            best_places = place_generator(statistic_integration=statistic_integration, best_places=best_places)
        print("END-----------------")

        place_id = best_places[0]
        info_places = select_info_with_place_id(place_id=best_places[0])

        for i in info_places:
            print("Проверка-----------------------")
            print(place_id)
            print(i[0])
            print("Проверка-----------------------")
            return i[0], i[1], i[2]
    except Exception as e:
        print(e)


def place_generator(statistic_integration: list, best_places: str):
    "Логика подбора лучшей карточки"
    for i in statistic_integration:
        if not best_places:
            best_places = [i[0], i[1], i[2]]
        else:
            if int(best_places[1]) < int(i[1]) and int(best_places[2]) > int(i[2]):
                if select_common_location_with_place_id(place_id=i[0])[0] == current_user.common_location:
                    best_places = [i[0], i[1], i[2]]
                else:
                    best_places = [i[0], i[1], i[2]]
    print(f"По тестам лучшая карточка:\n{best_places}")
    return best_places