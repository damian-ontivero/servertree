from flask import flash, jsonify, redirect, render_template, request

from app import db

from . import connection_type_bp
from flask_login import login_required
from app.auth.decorators import admin_required

from .models import ConnectionType
from .forms import ConnectionTypeForm

from app.auth.forms import UserForm
from app.environments.models import Environment

@connection_type_bp.route('/get_connection_type_all', methods=['GET'])
@login_required
def get_connection_type_all():
    data = ConnectionType.get_all()
    environments = Environment.get_all()
    connection_type_form = ConnectionTypeForm()
    user_form = UserForm()
    return render_template('connection-type.html', data=data, environments=environments, connection_type_form=connection_type_form, user_form=user_form)


@connection_type_bp.route('/get_connection_type_by_id', methods=['GET', 'POST'])
@login_required
@admin_required
def get_connection_type_by_id():
    connection_type_id = request.form['connection_type_id']
    connection_type = ConnectionType.get_by_id(connection_type_id)
    return jsonify(
        name = connection_type.name,
        is_active = connection_type.is_active
    )


@connection_type_bp.route('/add_connection_type', methods=['GET', 'POST'])
@login_required
@admin_required
def add_connection_type():
    connection_type_form = ConnectionTypeForm()
    if connection_type_form.validate_on_submit():
        name = connection_type_form.name
        is_active = connection_type_form.is_active
        connection_type = ConnectionType(name=name, is_active=is_active)
        if connection_type is not None:
            flash('El tipo de conexión {} ya está registrado.'.format(name), 'danger')
        else:
            connection_type.save()
            flash('Se ha registrado correctamente el tipo de conexión {}.'.format(name), 'success')

    return redirect(request.referrer)


@connection_type_bp.route('/edit_connection_type/<int:connection_type_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_connection_type(connection_type_id):
    connection_type = ConnectionType.get_by_id(connection_type_id)
    connection_type_form = ConnectionTypeForm(obj=connection_type)
    if connection_type_form.validate_on_submit():
        connection_type.name = connection_type_form.connection_type_name.data
        connection_type.is_active = connection_type_form.connection_type_is_active.data
        connection_type.save()
        flash('Se ha actualizado correctamente el tipo de conexión {}.'.format(connection_type_form.connection_type_name.data), 'success')
    return redirect(request.referrer)

@connection_type_bp.route('/delete_connection_type/<int:connection_type_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_connection_type(connection_type_id):
    connection_type = ConnectionType.get_by_id(connection_type_id)
    if connection_type is not None:
        connection_type.delete()
        flash('Se ha eliminado correctamente el tipo de conexión {}.'.format(connection_type.name), 'success')
        return redirect(request.referrer)
