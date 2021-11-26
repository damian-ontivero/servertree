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


@environment_bp.route("/get_all", methods=["GET", "POST"])
@login_required
def get_all():
    data = EnvironmentModel.get_all()
    environments = data
    environment_form = EnvironmentForm()
    user_form = UserForm()
    return render_template(
        "environments.html",
        data=data,
        environments=environments,
        environment_form=environment_form,
        user_form=user_form
    )


@environment_bp.route("/get/<int:environment_id>", methods=["GET", "POST"])
@login_required
@admin_required
def get(environment_id: int):
    environment = EnvironmentModel.get_by_id(environment_id)
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
        if EnvironmentModel.get_by_name(name) is not None:
            flash(f"El entorno {name} ya está registrado.", "danger")
        else:
            environment = EnvironmentModel(name=name, is_active=is_active)
            environment.save()
            flash(f"Se ha registrador correctamente el entorno {name}.", "success")

    return redirect(request.referrer)


@environment_bp.route("/edit/<int:environment_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(environment_id: int):
    environment = EnvironmentModel.get_by_id(environment_id)
    environment_form = EnvironmentForm(obj=environment)
    if environment_form.validate_on_submit():
        if environment.name == environment_form.environment_name.data:
            environment.name = environment_form.environment_name.data
            environment.is_active = environment_form.environment_is_active.data
            environment.save()
            flash(f"Se ha actualizado correctamente el entorno {environment.name}.", "success")
        else:
            if EnvironmentModel.get_by_name(environment_form.environment_name.data) is not None:
                flash(f"El entorno {environment_form.environment_name.data} ya está registrado.", "danger")
            else:
                environment.name = environment_form.environment_name.data
                environment.is_active = environment_form.environment_is_active.data
                environment.save()
                flash(f"Se ha actualizado correctamente el entorno {environment.name}.", "success")

    return redirect(request.referrer)


@environment_bp.route("/delete/<int:environment_id>", methods=["GET", "POST"])
@login_required
@admin_required
def delete(environment_id: int):
    environment = EnvironmentModel.get_by_id(environment_id)
    if environment is not None:
        environment.delete()
        flash(f"Se ha eliminado correctamente el entorno {environment.name}.", "success")
        return redirect(request.referrer)