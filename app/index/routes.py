from flask import render_template

from . import index_bp

from flask_login import login_required

from app.environments.models import Environment
from app.auth.forms import UserForm

@index_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    user_form = UserForm()
    environments = Environment.get_all()
    return render_template('index.html', user_form=user_form, environments=environments)