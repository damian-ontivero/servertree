"""Doc."""

from flask import Blueprint


environment_bp = Blueprint('environment', __name__, url_prefix='/environment', template_folder='templates')

from . import routes # noqa: 402
