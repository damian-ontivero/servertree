"""Server services management."""

from flask import (
    redirect,
    request,
    jsonify,
    flash
)
from flask_login import login_required

from app.servertree.auth.decorators import admin_required
from app.servertree.service import service_bp


@service_bp.route("/get/<int:service_id>", methods=["GET", "POST"])
@login_required
def get(service_id: int):
    """Doc."""
    service = ServiceModel.get_by_id(service_id)

    if service:
        return jsonify(
            service_id=service.id,
            server_id=service.server_id,
            service=service.service,
            version=service.version,
            architect=service.architect,
            ip_local=service.ip_local,
            port_local=service.port_local,
            ip_public=service.ip_public,
            port_public=service.port_public,
            install_dir=service.install_dir,
            log_dir=service.log_dir,
            is_active=service.is_active
        )
    else:
        return jsonify()


@service_bp.route("/get_by_server_id/<int:server_id>", methods=["GET", "POST"])
@login_required
def get_by_server_id(server_id: int):
    data_service = db.session.query(ServiceModel, ServerModel).join(ServerModel).filter(ServiceModel.server_id == server_id).all()

    if data_service:
        all_service = []
        for service, server in data_service:
            if service.is_active:
                is_active = "Si"
            else:
                is_active = "No"
            all_service.append({
                "service_id": service.id,
                "server_name": server.name,
                "service": service.service,
                "version": service.version,
                "architect": service.architect,
                "ip_local": service.ip_local,
                "port_local": service.port_local,
                "ip_public": service.ip_public,
                "port_public": service.port_public,
                "install_dir": service.install_dir,
                "log_dir": service.log_dir,
                "is_active": is_active
            })
        return jsonify(all_service)
    else:
        return jsonify()


@service_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add():
    service_form = ServiceForm()
    if service_form.validate_on_submit:
        server_id = service_form.service_server_id.data.id
        service = service_form.service.data
        version = service_form.service_version.data
        architect = service_form.service_architect.data
        ip_local = service_form.service_ip_local.data
        port_local = service_form.service_port_local.data
        ip_public = service_form.service_ip_public.data
        port_public = service_form.service_port_public.data
        install_dir = service_form.service_install_dir.data
        log_dir = service_form.service_log_dir.data
        is_active = service_form.service_is_active.data

        service = ServiceModel(
            server_id=server_id,
            service=service,
            version=version,
            architect=architect,
            ip_local=ip_local,
            port_local=port_local,
            ip_public=ip_public,
            port_public=port_public,
            install_dir=install_dir,
            log_dir=log_dir,
            is_active=is_active
        )
        service.save()

        flash("Se ha registrado correctamente el servicio.", "success")

    return redirect(request.referrer)


@service_bp.route("/edit/<int:service_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit(service_id: int):
    service = ServiceModel.get_by_id(service_id)
    server = ServerModel.get_by_id(service.server_id)
    service_form = ServiceForm(obj=service)
    if service_form.validate_on_submit():
        service.server_id = service_form.service_server_id.data.id
        service.service = service_form.service.data
        service.version = service_form.service_version.data
        service.architect = service_form.service_architect.data
        service.ip_local = service_form.service_ip_local.data
        service.port_local = service_form.service_port_local.data
        service.ip_public = service_form.service_ip_public.data
        service.port_public = service_form.service_port_public.data
        service.install_dir = service_form.service_install_dir.data
        service.log_dir = service_form.service_log_dir.data
        service.is_active = service_form.service_is_active.data
        service.save()
        flash("Se ha actualizado correctamente el servicio.", "success")

    return redirect(request.referrer)


@service_bp.route("/delete/<int:service_id>")
@login_required
@admin_required
def delete(service_id: int):
    service = ServiceModel.get_by_id(service_id)
    server = ServerModel.get_by_id(service.server_id)
    if service:
        service.delete()
        flash("Se ha eliminado correctamente el servicio.", "success")
        return redirect(request.referrer)
