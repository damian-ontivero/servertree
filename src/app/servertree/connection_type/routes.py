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
from model.environment.environment import EnvironmentModel


@connection_type_bp.route("/get_all", methods=["GET"])
@login_required
def get_all():
    data = ConnectionTypeModel.get_all()
    environments = EnvironmentModel.get_all()
    connection_type_form = ConnectionTypeForm()
    user_form = UserForm()
    return render_template(
        "connection-type.html",
        data=data,
        environments=environments,
        connection_type_form=connection_type_form,
        user_form=user_form
    )


@connection_type_bp.route("/get/<int:connection_type_id>", methods=["GET", "POST"])
@login_required
@admin_required
def get(connection_type_id: int):
    connection_type = ConnectionTypeModel.get_by_id(connection_type_id)
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
        if ConnectionTypeModel.get_by_name(name) is not None:
            flash(f"El tipo de conexión {name} ya está registrado.", "danger")
        else:
            connection_type = ConnectionTypeModel(name=name, is_active=is_active)
            connection_type.save()
            flash(f"Se ha registrado correctamente el tipo de conexión {name}.", "success")

    return redirect(request.referrer)


@connection_type_bp.route("/edit/<int:connection_type_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(connection_type_id: int):
    connection_type = ConnectionTypeModel.get_by_id(connection_type_id)
    connection_type_form = ConnectionTypeForm(obj=connection_type)
    if connection_type_form.validate_on_submit():
        if connection_type.name == connection_type_form.connection_type_name.data:
            connection_type.name = connection_type_form.connection_type_name.data
            connection_type.is_active = connection_type_form.connection_type_is_active.data
            connection_type.save()
            flash(f"Se ha actualizado correctamente el tipo de conexión {connection_type.name}.", "success")
        else:
            if ConnectionTypeModel.get_by_name(connection_type_form.connection_type_name.data) is not None:
                flash(f"El tipo de conexión {connection_type_form.connection_type_name.data} ya está registrado.", "danger")
            else:
                connection_type.name = connection_type_form.connection_type_name.data
                connection_type.is_active = connection_type_form.connection_type_is_active.data
                connection_type.save()
                flash("Se ha actualizado correctamente el tipo de conexión {}.".format(connection_type.name), "success")

    return redirect(request.referrer)


@connection_type_bp.route("/delete/<int:connection_type_id>", methods=["GET", "POST"])
@login_required
@admin_required
def delete(connection_type_id: int):
    connection_type = ConnectionTypeModel.get_by_id(connection_type_id)
    if connection_type is not None:
        connection_type.delete()
        flash(f"Se ha eliminado correctamente el tipo de conexión {connection_type.name}.", "success")
        return redirect(request.referrer)
