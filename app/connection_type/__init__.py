from flask import Blueprint

connection_type_bp = Blueprint('connection_type', __name__, url_prefix='/connection_type', template_folder='templates')

from . import routes