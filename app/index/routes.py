from flask import render_template

from . import index_bp

from flask_login import login_required

@index_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('index.html')