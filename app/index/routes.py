from flask import render_template

from . import index_bp

from flask_login import login_required

from app.environments.models import Environment

@index_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    environments = Environment.get_all()
    return render_template('index.html', environments=environments)