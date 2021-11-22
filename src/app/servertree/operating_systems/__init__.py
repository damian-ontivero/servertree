"""Doc."""

from flask import Blueprint


operating_system_bp = Blueprint("operating_system", __name__, url_prefix="/operating_system", template_folder="templates")

from . import routes # noqa: 402
