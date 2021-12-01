"""Doc."""

from flask import (
    render_template,
    redirect,
    request,
    jsonify,
    flash
)
from flask_login import login_required

from app.servertree.connection_type import connection_type_bp
from app.servertree.connection_type.forms import ConnectionTypeForm
from app.servertree.auth.decorators import admin_required
from app.servertree.auth.forms import UserForm

from model.connection_type.connection_type import ConnectionTypeModel

from service.connection_type.connection_type import connection_type_service
from service.environment.environment import environment_service


@connection_type_bp.route("/get_all", methods=["GET"])
@login_required
def get_all():
    return render_template(
        "connection-type.html",
        connection_type_list=connection_type_service.get_all(),
        environment_list=environment_service.get_all(),
        connection_type_form=ConnectionTypeForm(),
        user_form=UserForm()
    )


@connection_type_bp.route("/get/<int:connection_type_id>", methods=["GET", "POST"])
@login_required
@admin_required
def get(connection_type_id: int):
    connection_type = connection_type_service.get(id=connection_type_id)

    return jsonify(
        name=connection_type.name,
        is_active=connection_type.is_active
    )


@connection_type_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add():
    connection_type_form = ConnectionTypeForm()

    if connection_type_form.validate_on_submit():
        name = connection_type_form.connection_type_name.data
        is_active = connection_type_form.connection_type_is_active.data

        if connection_type_service.get_by_filter(name=name):
            flash("El tipo de conexión ya se encuentra registrado.", "danger")
        else:
            connection_type = ConnectionTypeModel(name=name, is_active=is_active)
            connection_type_service.add(obj_in=connection_type)
            flash("Se ha registrado correctamente el tipo de conexión.", "success")

    return redirect(request.referrer)


@connection_type_bp.route("/edit/<int:connection_type_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(connection_type_id: int):
    connection_type = connection_type_service.get(id=connection_type_id)
    connection_type_form = ConnectionTypeForm(obj=connection_type)

    if connection_type_form.validate_on_submit():
        if connection_type.name == connection_type_form.connection_type_name.data:
            connection_type.name = connection_type_form.connection_type_name.data
            connection_type.is_active = connection_type_form.connection_type_is_active.data
            connection_type_service.edit(obj_in=connection_type)
            flash("Se ha actualizado correctamente el tipo de conexión.", "success")
        else:
            if connection_type_service.get_by_filter(name=connection_type_form.connection_type_name.data):
                flash("El tipo de conexión ya se encuentra registrado.", "danger")
            else:
                connection_type.name = connection_type_form.connection_type_name.data
                connection_type.is_active = connection_type_form.connection_type_is_active.data
                connection_type_service.edit(obj_in=connection_type)
                flash("Se ha actualizado correctamente el tipo de conexión.", "success")

    return redirect(request.referrer)


@connection_type_bp.route("/delete/<int:connection_type_id>", methods=["GET", "POST"])
@login_required
@admin_required
def delete(connection_type_id: int):
    connection_type = connection_type_service.get(id=connection_type_id)
    connection_type_service.delete(obj_in=connection_type)

    flash("Se ha eliminado correctamente el tipo de conexión.", "success")

    return redirect(request.referrer)
