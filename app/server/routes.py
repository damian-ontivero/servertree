from flask import render_template, redirect, url_for, request, jsonify, flash
from flask_login import login_required
from app.auth.decorators import admin_required
from app import db
from . import server_bp
from .models import Server, Access, Service
from app.environments.models import Environment
from app.operating_systems.models import OperatingSystem
from app.connection_type.models import ConnectionType
from .forms import ServerForm, AccessForm, ServiceForm
from app.auth.forms import UserForm

'''

Server management

'''

@server_bp.route('/get_server_all', methods=['GET', 'POST'])
@login_required
def get_server_all():
    data = db.session.query(Server, Environment, OperatingSystem).join(Environment, OperatingSystem).all()
    environments = Environment.get_all()
    server_form = ServerForm()
    access_form = AccessForm()
    service_form = ServiceForm()
    user_form = UserForm()
    return render_template('server.html', data=data, environments=environments, server_form=server_form, access_form=access_form, service_form=service_form, user_form=user_form)

@server_bp.route('/get_server_by_env/<int:server_env>', methods=['GET', 'POST'])
@login_required
@admin_required
def get_server_by_env(server_env):
    data = db.session.query(Server, Environment, OperatingSystem).join(Environment, OperatingSystem).filter(Server.environment_id==server_env).all()
    environments = Environment.get_all()
    server_form = ServerForm()
    access_form = AccessForm()
    service_form = ServiceForm()
    user_form = UserForm()
    return render_template('server.html', data=data, environments=environments, server_form=server_form, access_form=access_form, service_form=service_form, user_form=user_form)

@server_bp.route('/get_server_by_id', methods=['GET', 'POST'])
@login_required
@admin_required
def get_server_by_id():
    server_id = request.form['server_id']
    server = Server.get_by_id(server_id)
    return jsonify(
        name = server.name,
        environment_id = server.environment_id,
        operating_system_id = server.operating_system_id,
        cpu = server.cpu,
        ram = server.ram,
        hdd = server.hdd,
        is_active = server.is_active
    )

@server_bp.route('/add_server', methods=['GET', 'POST'])
@login_required
@admin_required
def add_server():
    server_form = ServerForm()
    if server_form.validate_on_submit():
        name = server_form.server_name.data
        environment_id = server_form.server_environment_id.data.id
        operating_system_id = server_form.server_operating_system_id.data.id
        cpu = server_form.server_cpu.data
        ram = server_form.server_ram.data
        hdd = server_form.server_hdd.data
        is_active = server_form.server_is_active.data

        server = Server.get_by_name(name)
        if server is not None:
            flash('El servidor {} ya está registrado'.format(name), 'danger')
        else:
            server = Server(name=name, environment_id=environment_id, operating_system_id=operating_system_id, cpu=cpu, ram=ram, hdd=hdd, is_active=is_active)
            server.save()
            flash('Se ha registrado correctamente el servidor {}.'.format(name), 'success')

    return redirect(request.referrer)

@server_bp.route('/edit_server/<int:server_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_server(server_id):
    server = Server.get_by_id(server_id)
    server_form = ServerForm(obj=server)
    if server_form.validate_on_submit():
        server.name = server_form.server_name.data
        server.environment_id = server_form.server_environment_id.data.id
        server.operating_system_id = server_form.server_operating_system_id.data.id
        server.cpu = server_form.server_cpu.data
        server.ram = server_form.server_ram.data
        server.hdd = server_form.server_hdd.data
        server.is_active = server_form.server_is_active.data
        server.save()
        flash('Se ha actualizado correctamente el servidor {}.'.format(server.server_name), 'success')

    return redirect(request.referrer)

@server_bp.route('/delete_server/<int:server_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_server(server_id):
    server = Server.get_by_id(server_id)
    if server is not None:
        server.delete()
        flash('Se ha eliminado correctamente el servidor {}.'.format(server.name), 'success')
        return redirect(request.referrer)

'''

Server access management

'''

@server_bp.route('/get_access_by_server_id', methods=['GET', 'POST'])
@login_required
def get_access_by_server_id():
    server_id = request.form['server_id']
    data_access = db.session.query(Access, Server, ConnectionType).join(Server, ConnectionType).filter(Access.server_id==server_id).all()
    if data_access is not None:
        all_access = []
        for access, server, connection_type in data_access:
            if access.is_active:
                is_active = 'Si'
            else:
                is_active = 'No'
            all_access.append({
                'access_id': access.id,
                'server_name': server.name,
                'connection_type_name': connection_type.name,
                'ip_local': access.ip_local,
                'port_local': access.port_local,
                'ip_public': access.ip_public,
                'port_public': access.port_public,
                'username': access.username,
                'password': access.password,
                'is_active': is_active
            })
        return jsonify(all_access)
    else:
        return jsonify()


@server_bp.route('/get_access_by_id', methods=['GET', 'POST'])
@login_required
def get_access_by_id():
    access_id = request.form['access_id']
    access = Access.get_by_id(access_id)
    if access is not None:
        return jsonify(
            access_id = access.id,
            server_id = access.server_id,
            connection_type_id = access.connection_type_id,
            ip_local = access.ip_local,
            port_local = access.port_local,
            ip_public = access.ip_public,
            port_public = access.port_public,
            username = access.username,
            password = access.password,
            is_active = access.is_active
        )
    else:
        return jsonify()

@server_bp.route('/add_access', methods=['GET', 'POST'])
@login_required
@admin_required
def add_access():
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

        access = Access(server_id=server_id, connection_type_id=connection_type_id, ip_local=ip_local, port_local=port_local, ip_public=ip_public, port_public=port_public, username=username, password=password, is_active=is_active)
        access.save()
        flash('Se ha registrado correctamente el acceso para el servidor {}.'.format(access_form.access_server_id.data.name), 'success')
    return redirect(request.referrer)

@server_bp.route('/edit_access/<int:access_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_access(access_id):
    access = Access.get_by_id(access_id)
    server = Server.get_by_id(access.server_id)
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
        flash('Se ha actualizado correctamente el acceso para el servidor {}.'.format(server.name), 'success')

    return redirect(request.referrer)

@server_bp.route('/delete_access/<int:access_id>')
@login_required
@admin_required
def delete_access(access_id):
    access = Access.get_by_id(access_id)
    server = Server.get_by_id(access.server_id)
    if access is not None:
        access.delete()
        flash('Se ha eliminado correctamente el accesso para el servidor {}.'.format(server.name), 'success')
        return redirect(request.referrer)

'''

Server services management

'''

@server_bp.route('/get_service_by_server_id', methods=['GET', 'POST'])
@login_required
def get_service_by_server_id():
    server_id = request.form['server_id']
    data_service = db.session.query(Service, Server).join(Server).filter(Service.server_id==server_id).all()
    if data_service is not None:
        all_service = []
        for service, server in data_service:
            if service.is_active:
                is_active = 'Si'
            else:
                is_active = 'No'
            all_service.append({
                'service_id': service.id,
                'server_name': server.name,
                'service': service.service,
                'version': service.version,
                'architect': service.architect,
                'ip_local': service.ip_local,
                'port_local': service.port_local,
                'ip_public': service.ip_public,
                'port_public': service.port_public,
                'install_dir': service.install_dir,
                'log_dir': service.log_dir,
                'is_active': is_active
            })
        return jsonify(all_service)
    else:
        return jsonify()


@server_bp.route('/get_service_by_id', methods=['GET', 'POST'])
@login_required
def get_service_by_id():
    service_id = request.form['service_id']
    service = Service.get_by_id(service_id)
    if service is not None:
        return jsonify(
            service_id = service.id,
            server_id = service.server_id,
            service = service.service,
            version = service.version,
            architect = service.architect,
            ip_local = service.ip_local,
            port_local = service.port_local,
            ip_public = service.ip_public,
            port_public = service.port_public,
            install_dir = service.install_dir,
            log_dir = service.log_dir,
            is_active = service.is_active
        )
    else:
        return jsonify()

@server_bp.route('/add_service', methods=['GET', 'POST'])
@login_required
@admin_required
def add_service():
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

        service = Service(server_id=server_id, service=service, version=version, architect=architect, ip_local=ip_local, port_local=port_local, ip_public=ip_public, port_public=port_public, install_dir=install_dir, log_dir=log_dir, is_active=is_active)
        service.save()
        flash('Se ha registrado correctamente el servicio para el servidor {}.'.format(service_form.service_server_id.data.name), 'success')
    return redirect(request.referrer)

@server_bp.route('/edit_service/<int:service_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_service(service_id):
    service = Service.get_by_id(service_id)
    server = Server.get_by_id(service.server_id)
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
        flash('Se ha actualizado correctamente el servicio para el servidor {}.'.format(server.name), 'success')

    return redirect(request.referrer)

@server_bp.route('/delete_service/<int:service_id>')
@login_required
@admin_required
def delete_service(service_id):
    service = Service.get_by_id(service_id)
    server = Server.get_by_id(service.server_id)
    if service is not None:
        service.delete()
        flash('Se ha eliminado correctamente el servicio para el servidor {}.'.format(server.name), 'success')
        return redirect(request.referrer)