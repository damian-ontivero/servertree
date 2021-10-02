"""Docs."""

from flask import render_template
from flask_login import login_required

from servertree.app.index import index_bp
from servertree.app.environments.models import Environment
from servertree.app.auth.forms import UserForm


@index_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    user_form = UserForm()
    environments = Environment.get_all()
    return render_template('index.html', user_form=user_form, environments=environments)
