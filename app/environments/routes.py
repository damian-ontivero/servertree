from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_login import login_required

from . import environment_bp

from .models import Environment
from .forms import EnvironmentForm
from app.auth.forms import UserForm
from app.auth.decorators import admin_required

@environment_bp.route('/get_all', methods=['GET', 'POST'])
@login_required
def get_all():
    data = Environment.get_all()
    environments = data
    environment_form = EnvironmentForm()
    user_form = UserForm()
    return render_template('environments.html', data=data, environments=environments, environment_form=environment_form, user_form=user_form)

@environment_bp.route('/get_by_id', methods=['GET', 'POST'])
@login_required
@admin_required
def get_by_id():
    environment_id = request.form['environment_id']
    environment = Environment.get_by_id(environment_id)
    return jsonify(
        name = environment.name,
        is_active = environment.is_active
    )

@environment_bp.route('/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add():
    environment_form = EnvironmentForm()
    if environment_form.validate_on_submit():
        name = environment_form.environment_name.data
        is_active = environment_form.environment_is_active.data
        if Environment.get_by_name(name) is not None:
            flash('El entorno {} ya está registrado.'.format(name), 'danger')
        else:
            environment = Environment(name=name, is_active=is_active)
            environment.save()
            flash('Se ha registrador correctamente el entorno {}.'.format(name), 'success')

    return redirect(request.referrer)

@environment_bp.route('/edit/<int:environment_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit(environment_id):
    environment = Environment.get_by_id(environment_id)
    environment_form = EnvironmentForm(obj=environment)
    if environment_form.validate_on_submit():
        if environment.name == environment_form.environment_name.data:
            flash('No hubo cambios para el entorno {}.'.format(environment.name), 'warning')
            return redirect(request.referrer)

        environment.name = environment_form.environment_name.data
        environment.is_active = environment_form.environment_is_active.data
        if Environment.get_by_name(environment.name) is not None:
            flash('El entorno {} ya está registrado.'.format(environment.name), 'danger')
        else:
            environment.save()
            flash('Se ha actualizado correctamente el entorno {}.'.format(environment.name), 'success')

    return redirect(request.referrer)

@environment_bp.route('/delete/<int:environment_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete(environment_id):
    environment = Environment.get_by_id(environment_id)
    environment.delete()
    flash('Se ha eliminado correctamente el entorno {}.'.format(environment.name), 'success')
    return redirect(request.referrer)