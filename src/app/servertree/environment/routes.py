"""Doc."""

from flask import (
    render_template,
    redirect,
    request,
    jsonify,
    flash
)
from flask_login import login_required

from app.servertree.environment import environment_bp
from app.servertree.environment.forms import EnvironmentForm
from app.servertree.auth.forms import UserForm
from app.servertree.auth.decorators import admin_required

from model.environment.environment import EnvironmentModel

from service.environment.environment import environment_service


@environment_bp.route("/get_all", methods=["GET", "POST"])
@login_required
def get_all():
    return render_template(
        "environment.html",
        environment_list=environment_service.get_all(),
        environment_form=EnvironmentForm(),
        user_form=UserForm()
    )


@environment_bp.route("/get/<int:environment_id>", methods=["GET", "POST"])
@login_required
@admin_required
def get(environment_id: int):
    environment = environment_service.get(id=environment_id)

    return jsonify(
        name=environment.name,
        is_active=environment.is_active
    )


@environment_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add():
    environment_form = EnvironmentForm()

    if environment_form.validate_on_submit():
        name = environment_form.environment_name.data
        is_active = environment_form.environment_is_active.data
        if environment_service.get_by_filter(name=name):
            flash("El entorno ya se encuentra registrado.", "danger")
        else:
            environment = EnvironmentModel(name=name, is_active=is_active)
            environment_service.add(obj_in=environment)
            flash("Se ha registrado correctamente el entorno.", "success")

    return redirect(request.referrer)


@environment_bp.route("/edit/<int:environment_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(environment_id: int):
    environment = environment_service.get(id=environment_id)
    environment_form = EnvironmentForm(obj=environment)

    if environment_form.validate_on_submit():
        if environment.name == environment_form.environment_name.data:
            environment.name = environment_form.environment_name.data
            environment.is_active = environment_form.environment_is_active.data
            environment_service.edit(obj_in=environment)
            flash("Se ha actualizado correctamente el entorno.", "success")
        else:
            if environment_service.get_by_filter(name=environment_form.environment_name.data):
                flash("El entorno ya se encuentra registrado.", "danger")
            else:
                environment.name = environment_form.environment_name.data
                environment.is_active = environment_form.environment_is_active.data
                environment_service.edit(obj_in=environment)
                flash("Se ha actualizado correctamente el entorno.", "success")

    return redirect(request.referrer)


@environment_bp.route("/delete/<int:environment_id>", methods=["GET", "POST"])
@login_required
@admin_required
def delete(environment_id: int):
    environment = environment_service.get(id=environment_id)
    environment_service.delete(obj_in=environment)

    flash("Se ha eliminado correctamente el entorno.", "success")

    return redirect(request.referrer)
