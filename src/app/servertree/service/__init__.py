"""Doc."""

from flask import Blueprint


service_bp = Blueprint("service", __name__, url_prefix="/service", template_folder="templates")

from . import routes # noqa: 402
