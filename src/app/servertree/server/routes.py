"""Server management."""

from flask import render_template, redirect, request, jsonify, flash
from flask_login import login_required

from model import db
from model.server.server import ServerModel
from model.environment.environment import EnvironmentModel
from model.operating_system.operating_system import OperatingSystemModel
from app.servertree.server import server_bp
from app.servertree.server.forms import ServerForm
from app.servertree.access.forms import AccessForm
from app.servertree.service.forms import ServiceForm
from app.servertree.auth.forms import UserForm
from app.servertree.auth.decorators import admin_required
from service.environment.environment import EnvironmentService
from service.server.server import ServerService


@server_bp.route("/get_all", methods=["GET", "POST"])
@login_required
def get_all():
    server_list = ServerService.get_all()
    environment_list = EnvironmentService.get_all()
    server_form = ServerForm()
    access_form = AccessForm()
    service_form = ServiceForm()
    user_form = UserForm()
    return render_template(
        "server.html",
        server_list=server_list,
        environment_list=environment_list,
        server_form=server_form,
        access_form=access_form,
        service_form=service_form,
        user_form=user_form
    )


@server_bp.route("/get_by_env/<int:server_env>", methods=["GET", "POST"])
@login_required
def get_by_env(server_env: int):
    server_list = ServerService.get_by_filter_all(environment_id=server_env)
    environment_list = EnvironmentService.get_all()
    server_form = ServerForm()
    access_form = AccessForm()
    service_form = ServiceForm()
    user_form = UserForm()
    return render_template(
        "server.html",
        server_list=server_list,
        environment_list=environment_list,
        server_form=server_form,
        access_form=access_form,
        service_form=service_form,
        user_form=user_form
    )


@server_bp.route("/get/<int:server_id>", methods=["GET", "POST"])
@login_required
@admin_required
def get(server_id: int):
    server = ServerService.get(id=server_id)
    return jsonify(
        name=server.name,
        environment_id=server.environment_id,
        operating_system_id=server.operating_system_id,
        cpu=server.cpu,
        ram=server.ram,
        hdd=server.hdd,
        is_active=server.is_active
    )


@server_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add():
    server_form = ServerForm()

    if server_form.validate_on_submit():
        name = server_form.server_name.data
        environment_id = server_form.server_environment_id.data.id
        operating_system_id = server_form.server_operating_system_id.data.id
        cpu = server_form.server_cpu.data
        ram = server_form.server_ram.data
        hdd = server_form.server_hdd.data
        is_active = server_form.server_is_active.data

        server = ServerService.get_by_filter(name=name)
        
        if server:
            flash("El servidor ya se encuentra registrado.", "danger")
        else:
            server = ServerModel(
                name=name,
                environment_id=environment_id,
                operating_system_id=operating_system_id,
                cpu=cpu,
                ram=ram,
                hdd=hdd,
                is_active=is_active
            )
            ServerService.add(obj_in=server)
            flash("Se ha registrado correctamente el servidor.", "success")

    return redirect(request.referrer)


@server_bp.route("/edit/<int:server_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(server_id: int):
    server = ServerService.get(id=server_id)
    server_form = ServerForm(obj=server)

    if server_form.validate_on_submit():
        if server.name == server_form.server_name.data and server.environment_id == server_form.server_environment_id.data.id:
            server.name = server_form.server_name.data
            server.environment_id = server_form.server_environment_id.data.id
            server.operating_system_id = server_form.server_operating_system_id.data.id
            server.cpu = server_form.server_cpu.data
            server.ram = server_form.server_ram.data
            server.hdd = server_form.server_hdd.data
            server.is_active = server_form.server_is_active.data
            ServerService.edit(obj_in=server)
            flash("Se ha actualizado correctamente el servidor.", "success")
        else:
            if ServerService.get_by_filter(name=server_form.server_name.data) and ServerService.get_by_filter(
                    name=server_form.server_name.data).environment_id == server_form.server_environment_id.data.id:
                flash("El servidor ya se encuentra registrado.", "danger")
            else:
                server.name = server_form.server_name.data
                server.environment_id = server_form.server_environment_id.data.id
                server.operating_system_id = server_form.server_operating_system_id.data.id
                server.cpu = server_form.server_cpu.data
                server.ram = server_form.server_ram.data
                server.hdd = server_form.server_hdd.data
                server.is_active = server_form.server_is_active.data
                ServerService.edit(obj_in=server)
                flash("Se ha actualizado correctamente el servidor.", "success")

    return redirect(request.referrer)


@server_bp.route("/delete/<int:server_id>", methods=["GET", "POST"])
@login_required
@admin_required
def delete(server_id: int):
    server = ServerService.get(id=server_id)
    ServerService.delete(obj_in=server)
    flash("Se ha eliminado correctamente el servidor.", "success")
    return redirect(request.referrer)
