"""Doc."""

from flask import flash, jsonify, redirect, render_template, request
from flask_login import login_required

from app.servertree.operating_system import operating_system_bp
from app.servertree.operating_system.forms import OperatingSystemForm
from app.servertree.auth.forms import UserForm
from app.servertree.auth.decorators import admin_required
from model.operating_system.operating_system import OperatingSystemModel
from service.environment.environment import environment_service
from service.operating_system.operating_system import operating_system_service


@operating_system_bp.route("/get_all", methods=["GET", "POST"])
@login_required
def get_all():
    return render_template(
        "operating-system.html",
        operating_system_list=operating_system_service.get_all(),
        environment_list=environment_service.get_all(),
        operating_system_form=OperatingSystemForm(),
        user_form=UserForm()
    )


@operating_system_bp.route("/get/<int:operating_system_id>", methods=["GET", "POST"])
@login_required
def get(operating_system_id: int):
    operating_system = operating_system_service.get(id=operating_system_id)
    return jsonify(
        name=operating_system.name,
        version=operating_system.version,
        architect=operating_system.architect,
        is_active=operating_system.is_active
    )


@operating_system_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add():
    operating_system_form = OperatingSystemForm()
    if operating_system_form.validate_on_submit():
        name = operating_system_form.operating_system_name.data
        version = operating_system_form.operating_system_version.data
        architect = operating_system_form.operating_system_architect.data
        is_active = operating_system_form.operating_system_is_active.data
        if operating_system_service.get_by_filter(name=name, version=version, architect=architect):
            flash("El sistema operativo ya se encuentra registrado.", "danger")
        else:
            operating_system = OperatingSystemModel(name=name, version=version, architect=architect, is_active=is_active)
            operating_system_service.add(obj_in=operating_system)
            flash("Se ha registrado correctamente el sistema operativo.", "success")

    return redirect(request.referrer)


@operating_system_bp.route("/edit/<int:operating_system_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(operating_system_id: int):
    operating_system = operating_system_service.get(id=operating_system_id)
    operating_system_form = OperatingSystemForm(obj=operating_system)
    if operating_system_form.validate_on_submit():
        if (operating_system.name == operating_system_form.operating_system_name.data
                and operating_system.version == operating_system_form.operating_system_version.data
                and operating_system.architect == operating_system_form.operating_system_architect.data):
            operating_system.name = operating_system_form.operating_system_name.data
            operating_system.version = operating_system_form.operating_system_version.data
            operating_system.architect = operating_system_form.operating_system_architect.data
            operating_system.is_active = operating_system_form.operating_system_is_active.data
            operating_system_service.edit(obj_in=operating_system)
            flash("Se ha actualizado correctamente el sistema operativo.", "success")
        else:
            if operating_system_service.get_by_filter(
                name=operating_system_form.operating_system_name.data,
                version=operating_system_form.operating_system_version.data,
                architect=operating_system_form.operating_system_architect.data
            ):
                flash("El sistema operativo ya se encuentra registrado.", "danger")
            else:
                operating_system.name = operating_system_form.operating_system_name.data
                operating_system.version = operating_system_form.operating_system_version.data
                operating_system.architect = operating_system_form.operating_system_architect.data
                operating_system.is_active = operating_system_form.operating_system_is_active.data
                operating_system_service.edit(obj_in=operating_system)
                flash("Se ha actualizado correctamente el sistema operativo.", "success")

    return redirect(request.referrer)


@operating_system_bp.route("/delete/<int:operating_system_id>", methods=["GET", "POST"])
@login_required
@admin_required
def delete(operating_system_id: int):
    operating_system = operating_system_service.get(id=operating_system_id)
    operating_system_service.delete(obj_in=operating_system)
    flash("Se ha eliminado correctamente el sistema operativo.", "success")
    return redirect(request.referrer)
