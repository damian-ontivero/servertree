"""Doc."""

from flask import Blueprint


application_bp = Blueprint("application", __name__, url_prefix="/application", template_folder="templates")

from . import routes # noqa: 402
