"""Docs."""

from functools import wraps

from flask import abort
from flask_login import current_user


def admin_required(function):
    @wraps(function)
    def wrapper(*args, **kwds):
        if current_user.role_id != 1:
            abort(401)
        return function(*args, **kwds)
    return wrapper
