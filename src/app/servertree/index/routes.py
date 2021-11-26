"""Doc."""

from flask import render_template
from flask_login import login_required

from app.servertree.index import index_bp
from app.servertree.auth.forms import UserForm
from service.environment.environment import EnvironmentService


@index_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    user_form = UserForm()
    environment_list = EnvironmentService.get_all()
    return render_template("index.html", user_form=user_form, environment_list=environment_list)
