"""Doc."""

from flask import Blueprint


access_bp = Blueprint("access", __name__, url_prefix="/access", template_folder="templates")

from . import routes # noqa: 402
