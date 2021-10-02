"""Docs."""

from flask import Blueprint

index_bp = Blueprint('index', __name__, template_folder='templates')

from . import routes # noqa: 402