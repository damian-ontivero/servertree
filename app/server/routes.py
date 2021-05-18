from flask import render_template, redirect, url_for, request, jsonify, flash
from flask_login import login_required
from app.auth.decorators import admin_required
from app import db
from . import server_bp
from .models import Server, Environment, OperatingSystem, Access, ConnectionType
from .forms import ServerForm, AccessForm, AppForm

@server_bp.route('/get_server_all', methods=['GET', 'POST'])
@login_required
def get_server_all():
    data = db.session.query(Server, Environment, OperatingSystem).join(Environment, OperatingSystem).all()
    form = ServerForm()
    access_form = AccessForm()
    app_form = AppForm()
    return render_template('server.html', data=data, form=form, access_form=access_form, app_form=app_form)

@server_bp.route('/get_server_by_env/<int:server_env>', methods=['GET', 'POST'])
@login_required
@admin_required
def get_server_by_env(server_env):
    data = db.session.query(Server, Environment, OperatingSystem).join(Environment, OperatingSystem).filter(Server.environment_id==server_env).all()
    form = ServerForm()
    access_form = AccessForm()
    app_form = AppForm()
    return render_template('server.html', data=data, form=form, access_form=access_form, app_form=app_form)

@server_bp.route('/get_server', methods=['GET', 'POST'])
@login_required
@admin_required
def get_server():
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
    form = ServerForm()
    if form.validate_on_submit():
        name = form.name.data
        environment_id = form.environment_id.data.id
        operating_system_id = form.operating_system_id.data.id
        cpu = form.cpu.data
        ram = form.ram.data
        hdd = form.hdd.data
        is_active = form.is_active.data

        server = Server.get_by_name(name)
        if server is not None:
            error = 'El servidor {} ya está registrado'.format(name)
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
    form = ServerForm(obj=server)
    if form.validate_on_submit():
        server.name = form.name.data
        server.environment_id = form.environment_id.data.id
        server.operating_system_id = form.operating_system_id.data.id
        server.cpu = form.cpu.data
        server.ram = form.ram.data
        server.hdd = form.hdd.data
        server.is_active = form.is_active.data
        server.save()
        flash('Se ha actualizado correctamente el servidor {}.'.format(server.name), 'success')

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

@server_bp.route('/get_server_access_by_server_id', methods=['GET', 'POST'])
@login_required
@admin_required
def get_server_access_by_server_id():
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


@server_bp.route('/get_server_access_by_access_id', methods=['GET', 'POST'])
@login_required
@admin_required
def get_server_access_by_access_id():
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

@server_bp.route('/add_server_access', methods=['GET', 'POST'])
@login_required
@admin_required
def add_server_access():
    form = AccessForm()
    if form.validate_on_submit:
        server_id = form.server_id.data.id
        connection_type_id = form.connection_type_id.data.id
        ip_local = form.ip_local.data
        port_local = form.port_local.data
        ip_public = form.ip_public.data
        port_public = form.port_public.data
        username = form.username.data
        password = form.password.data
        is_active = form.is_active.data

        access = Access(server_id=server_id, connection_type_id=connection_type_id, ip_local=ip_local, port_local=port_local, ip_public=ip_public, port_public=port_public, username=username, password=password, is_active=is_active)
        access.save()
        flash('Se ha registrado correctamente el acceso para el servidor {}.'.format(form.server_id.data.name), 'success')
    return redirect(request.referrer)

@server_bp.route('/edit_server_access/<int:access_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_server_access(access_id):
    access = Access.get_by_id(access_id)
    server = Server.get_by_id(access.server_id)
    form = AccessForm(obj=access)
    if form.validate_on_submit():
        access.server_id = form.server_id.data.id
        access.connection_type_id = form.connection_type_id.data.id
        access.ip_local = form.ip_local.data
        access.port_local = form.port_local.data
        access.ip_public = form.ip_public.data
        access.port_public = form.port_public.data
        access.username = form.username.data
        access.password = form.password.data
        access.is_active = form.is_active.data
        access.save()
        flash('Se ha actualizado correctamente el acceso para el servidor {}.'.format(server.name), 'success')

    return redirect(request.referrer)

@server_bp.route('/delete_server_access/<int:access_id>')
@login_required
@admin_required
def delete_server_access(access_id):
    access = Access.get_by_id(access_id)
    server = Server.get_by_id(access.server_id)
    if access is not None:
        access.delete()
        flash('Se ha eliminado correctamente el accesso para el servidor {}.'.format(server.name), 'success')
        return redirect(request.referrer)