"""Doc."""

from flask import render_template
from flask_login import login_required

from app.servertree.index import index_bp
from app.servertree.auth.forms import UserForm
from service.environment.environment import environment_service


@index_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    return render_template(
        "index.html",
        environment_list=environment_service.get_all(),
        user_form=UserForm()
    )
