from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_login import login_required

from servertree.app.operating_systems import operating_system_bp
from servertree.app.operating_systems.models import OperatingSystem
from servertree.app.operating_systems.forms import OperatingSystemForm
from servertree.app.auth.forms import UserForm
from servertree.app.auth.decorators import admin_required
from servertree.app.environments.models import Environment


@operating_system_bp.route('/get_all', methods=['GET', 'POST'])
@login_required
def get_all():
    data = OperatingSystem.get_all()
    environments = Environment.get_all()
    operating_system_form = OperatingSystemForm()
    user_form = UserForm()
    return render_template('operating-systems.html', data=data, environments=environments, operating_system_form=operating_system_form, user_form=user_form)

@operating_system_bp.route('get_by_id', methods=['GET', 'POST'])
@login_required
def get_by_id():
    operating_system_id = request.form['operating_system_id']
    operating_system = OperatingSystem.get_by_id(operating_system_id)
    return jsonify(
        name = operating_system.name,
        version = operating_system.version,
        architect = operating_system.architect,
        is_active = operating_system.is_active
    )

@operating_system_bp.route('/add', methods=['GET', 'POST'])
@login_required
@admin_required
def add():
    operating_system_form = OperatingSystemForm()
    if operating_system_form.validate_on_submit():
        name = operating_system_form.operating_system_name.data
        version = operating_system_form.operating_system_version.data
        architect = operating_system_form.operating_system_architect.data
        is_active = operating_system_form.operating_system_is_active.data
        if OperatingSystem.get_by_name_version_architect(name, version, architect) is not None:
            flash('El sistema operativo {} {} {} ya está registrado.'.format(name, version, architect), 'danger')
        else:
            operating_system = OperatingSystem(name=name, version=version, architect=architect, is_active=is_active)
            operating_system.save()
            flash('Se ha registrador correctamente el sistema operativo {}.'.format(name), 'success')

    return redirect(request.referrer)

@operating_system_bp.route('/edit/<int:operating_system_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit(operating_system_id):
    operating_system = OperatingSystem.get_by_id(operating_system_id)
    operating_system_form = OperatingSystemForm(obj=operating_system)
    if operating_system_form.validate_on_submit():
        if operating_system.name == operating_system_form.operating_system_name.data and operating_system.version == operating_system_form.operating_system_version.data and operating_system.architect == operating_system_form.operating_system_architect.data:
            operating_system.name = operating_system_form.operating_system_name.data
            operating_system.version = operating_system_form.operating_system_version.data
            operating_system.architect = operating_system_form.operating_system_architect.data
            operating_system.is_active = operating_system_form.operating_system_is_active.data
            operating_system.save()
            flash('Se ha actualizado correctamente el sistema operativo {} {} {}.'.format(operating_system.name, operating_system.version, operating_system.architect), 'success')
        else: 
            if OperatingSystem.get_by_name_version_architect(operating_system_form.operating_system_name.data, operating_system_form.operating_system_version.data, operating_system_form.operating_system_architect.data) is not None:
                flash('El sistema operativo {} {} {} ya está registrado.'.format(operating_system_form.operating_system_name.data, operating_system_form.operating_system_version.data, operating_system_form.operating_system_architect.data), 'danger')
            else:
                operating_system.name = operating_system_form.operating_system_name.data
                operating_system.version = operating_system_form.operating_system_version.data
                operating_system.architect = operating_system_form.operating_system_architect.data
                operating_system.is_active = operating_system_form.operating_system_is_active.data
                operating_system.save()
                flash('Se ha actualizado correctamente el sistema operativo {} {} {}.'.format(operating_system.name, operating_system.version, operating_system.architect), 'success')

    return redirect(request.referrer)

@operating_system_bp.route('/delete/<int:operating_system_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete(operating_system_id):
    operating_system = OperatingSystem.get_by_id(operating_system_id)
    if operating_system is not None:
        operating_system.delete()
        flash('Se ha eliminado correctamente el sistema operativo {}.'.format(operating_system.name), 'success')
        return redirect(request.referrer)
