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


@access_bp.route("/get/<int:access_id>", methods=["GET", "POST"])
@login_required
def get(access_id: int):
    access = AccessModel.get_by_id(access_id)
    if access is not None:
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
    data_access = db.session.query(
        AccessModel,
        ServerModel,
        ConnectionTypeModel).join(ServerModel, ConnectionTypeModel).filter(AccessModel.server_id == server_id).all()
    if data_access is not None:
        all_access = []
        for access, server, connection_type in data_access:
            if access.is_active:
                is_active = "Si"
            else:
                is_active = "No"
            all_access.append({
                "access_id": access.id,
                "server_name": server.name,
                "connection_type_name": connection_type.name,
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
        access.save()

        flash(f"Se ha registrado correctamente el acceso para el servidor {access_form.access_server_id.data.name}.", "success")

    return redirect(request.referrer)


@access_bp.route("/edit/<int:access_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(access_id: int):
    access = AccessModel.get_by_id(access_id)
    server = ServerModel.get_by_id(access.server_id)
    access_form = AccessForm(obj=access)
    if access_form.validate_on_submit():
        access.server_id = access_form.access_server_id.data.id
        access.connection_type_id = access_form.access_connection_type_id.data.id
        access.ip_local = access_form.access_ip_local.data
        access.port_local = access_form.access_port_local.data
        access.ip_public = access_form.access_ip_public.data
        access.port_public = access_form.access_port_public.data
        access.username = access_form.access_username.data
        access.password = access_form.access_password.data
        access.is_active = access_form.access_is_active.data
        access.save()
        flash(f"Se ha actualizado correctamente el acceso para el servidor {server.name}.", "success")

    return redirect(request.referrer)


@access_bp.route("/delete/<int:access_id>")
@login_required
@admin_required
def delete(access_id: int):
    access = AccessModel.get_by_id(access_id)
    server = ServerModel.get_by_id(access.server_id)
    if access is not None:
        access.delete()
        flash(f"Se ha eliminado correctamente el accesso para el servidor {server.name}.", "success")
        return redirect(request.referrer)