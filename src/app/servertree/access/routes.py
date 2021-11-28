"""Server services management."""

from flask import (
    redirect,
    request,
    jsonify,
    flash
)
from flask_login import login_required

from app.servertree.auth.decorators import admin_required
from app.servertree.access import access_bp
from app.servertree.access.forms import AccessForm
from model.server.access import AccessModel
from service.server.access import access_service


@access_bp.route("/get/<int:access_id>", methods=["GET", "POST"])
@login_required
def get(access_id: int):
    access = access_service.get(id=access_id)
    if access:
        return jsonify(
            access_id=access.id,
            server_id=access.server_id,
            connection_type_id=access.connection_type_id,
            ip_local=access.ip_local,
            port_local=access.port_local,
            ip_public=access.ip_public,
            port_public=access.port_public,
            username=access.username,
            password=access.password,
            is_active=access.is_active
        )
    else:
        return jsonify()


@access_bp.route("/get_by_server_id/<int:server_id>", methods=["GET", "POST"])
@login_required
def get_by_server_id(server_id: int):
    access_list = access_service.get_by_filter_all(server_id=server_id)

    if access_list:
        all_access = []
        for access in access_list:
            if access.is_active:
                is_active = "Si"
            else:
                is_active = "No"
            all_access.append({
                "access_id": access.id,
                "server_name": access.server.name,
                "connection_type_name": access.connection_type.name,
                "ip_local": access.ip_local,
                "port_local": access.port_local,
                "ip_public": access.ip_public,
                "port_public": access.port_public,
                "username": access.username,
                "password": access.password,
                "is_active": is_active
            })
        return jsonify(all_access)
    else:
        return jsonify()


@access_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add():
    access_form = AccessForm()
    if access_form.validate_on_submit:
        server_id = access_form.access_server_id.data.id
        connection_type_id = access_form.access_connection_type_id.data.id
        ip_local = access_form.access_ip_local.data
        port_local = access_form.access_port_local.data
        ip_public = access_form.access_ip_public.data
        port_public = access_form.access_port_public.data
        username = access_form.access_username.data
        password = access_form.access_password.data
        is_active = access_form.access_is_active.data

        access = AccessModel(
            server_id=server_id,
            connection_type_id=connection_type_id,
            ip_local=ip_local,
            port_local=port_local,
            ip_public=ip_public,
            port_public=port_public,
            username=username,
            password=password,
            is_active=is_active
        )
        access_service.add(obj_in=access)

        flash("Se ha registrado correctamente el acceso.", "success")

    return redirect(request.referrer)


@access_bp.route("/edit/<int:access_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(access_id: int):
    access = access_service.get(id=access_id)
    access_form = AccessForm(obj=access)

    print("Validation form pending")

    if access_form.validate_on_submit():
        print("Validation form ok")
        access.server_id = access_form.access_server_id.data.id
        access.connection_type_id = access_form.access_connection_type_id.data.id
        access.ip_local = access_form.access_ip_local.data
        access.port_local = access_form.access_port_local.data
        access.ip_public = access_form.access_ip_public.data
        access.port_public = access_form.access_port_public.data
        access.username = access_form.access_username.data
        access.password = access_form.access_password.data
        access.is_active = access_form.access_is_active.data

        access_service.edit(obj_in=access)

        flash("Se ha actualizado correctamente el acceso.", "success")

    return redirect(request.referrer)


@access_bp.route("/delete/<int:access_id>")
@login_required
@admin_required
def delete(access_id: int):
    access = access_service.get(id=access_id)
    access_service.delete(access)
    flash("Se ha eliminado correctamente el accesso.", "success")
    return redirect(request.referrer)
