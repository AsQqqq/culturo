from pages_backend.index import route_index
from pages_backend.login import route_login, logout_login
from pages_backend.register import route_register
from pages_backend.not_found import route_not_found
from pages_backend.tested import route_tested
from .api import upload_api
from .profile.route_profile import upload_profile
from .places.route_places import upload_places
from .admin.route_admin import upload_admin