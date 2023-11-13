from database.dibs import database_query_user_place, database_query


def get_all_locale_true_places(username: str):
    sql = f"SELECT * FROM {username} WHERE liked = true"
    cursor = database_query_user_place(sql_query=sql, types="return")
    result = cursor.fetchall()
    if result:
        return result
    else:
        return False


def get_info_position(ip_point: str):
    sql = f"SELECT name, name_photo, description, hours_of_operation_start, hours_of_operation_end, contact_phone, email, date_open, location, site, break_time_start, break_time_end  FROM places WHERE id_point = '{ip_point}'"
    cursor = database_query(sql_query=sql, types="return")
    result = cursor.fetchall()
    return result