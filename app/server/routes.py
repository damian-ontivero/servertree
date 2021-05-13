from flask import render_template, redirect, url_for, request, jsonify, flash
from flask_login import login_required
from app.auth.decorators import admin_required
from app import db
from . import server_bp
from .models import Server, Environment, OperatingSystem
from .forms import ServerForm

@server_bp.route('/get_server_all', methods=['GET', 'POST'])
@login_required
def get_server_all():
    data = db.session.query(Server, Environment, OperatingSystem).join(Environment, OperatingSystem).all()
    form = ServerForm()
    return render_template('server.html', data=data, form=form)

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

@server_bp.route('/get_server_by_env/<int:server_env>', methods=['GET', 'POST'])
@login_required
@admin_required
def get_server_by_env(server_env):
    data = db.session.query(Server, Environment, OperatingSystem).join(Environment, OperatingSystem).filter(Server.environment_id==server_env).all()
    form = ServerForm()
    return render_template('server.html', data=data, form=form)

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
        return redirect(request.referrer)