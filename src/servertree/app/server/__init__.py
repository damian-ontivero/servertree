from flask import Blueprint

server_bp = Blueprint('server', __name__, url_prefix='/server', template_folder='templates')

from . import routes