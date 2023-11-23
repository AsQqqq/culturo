"""Импорт всех файлов для загрузки сайта"""

from pages_backend.index import route, algorithm
from pages_backend.login import route, logout
from pages_backend.register import route
from pages_backend.not_found import route_not_found
from pages_backend.tested import route
# from .api import api
# from .profile.route_profile import upload_profile
# from .places.route_places import upload_places
# from .admin.route_admin import upload_admin