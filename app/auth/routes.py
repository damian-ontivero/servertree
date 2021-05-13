from flask import render_template, redirect, request, url_for, jsonify, flash
from requests import Response
import jsonpickle
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from app import login_manager, db
from . import auth_bp
from .forms import LoginForm, UserForm
from .models import User, Role
from .decorators import admin_required

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index.index'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.get_by_email(email)
        if user is not None and user.check_password(form.password.data) and user.is_active:
            login_user(user, remember=form.remember_me.data)
            flash('Se ha iniciado sesión correctamente con el usuario {}.'.format(email), 'success')
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index.index')
            return redirect(next_page)
        elif user is None or not user.check_password(form.password.data):
            flash('Email o contraseña incorrecto.', 'danger')
        elif not user.is_active:
            flash('Usuario inactivo.', 'danger')

    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))

@auth_bp.route('/get_user_all', methods=['GET', 'POST'])
@login_required
def get_user_all():
    data = db.session.query(User, Role).join(Role).all()
    form = UserForm()
    return render_template('user.html', data=data, form=form)

@auth_bp.route('/get_user', methods=['GET', 'POST'])
@login_required
@admin_required
def get_user():
    user_id = request.form['user_id']
    user = User.get_by_id(user_id)
    return jsonify(
        firstname = user.firstname,
        lastname = user.lastname,
        email = user.email,
        password = user.password,
        role_id = user.role_id,
        is_active = user.is_active
    )

@auth_bp.route('/add_user', methods=['GET', 'POST'])
@login_required
@admin_required
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        # Recuperamos los datos del formulario
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        # Importante! Se accede a '...data.id' porque desde el campo 'QuerySelectField'
        # llega el objeto completo y debemos acceder a la propiedad 'id'
        role_id = form.role_id.data.id
        is_active = form.is_active.data
        # Comprobamos que no hay ya un usuario con ese email
        user = User.get_by_email(email)
        if user is not None:
            flash('El email {} ya está registrado por otro usuario.'.format(email), 'danger')
        else:
            # Creamos el usuario y lo guardamos
            user = User(firstname=firstname, lastname=lastname, email=email, role_id=role_id, is_active=is_active)
            user.set_password(password)
            user.save()
            flash('Se ha registrado correctamente el usuario con email {}.'.format(email), 'success')
            # Devolvemos la vista de todos los usuarios
    return redirect(url_for('auth.get_user_all'))

@auth_bp.route('/edit_user/<user_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_user(user_id):
    user = User.get_by_id(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        # Recuperamos los datos del formulario
        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.email = form.email.data
        if form.change_password.data:
            user.set_password(form.password.data)
        # Importante! Se accede a '...data.id' porque desde el campo 'QuerySelectField'
        # llega el objeto completo y debemos acceder a la propiedad 'id'
        user.role_id = form.role_id.data.id
        user.is_active = form.is_active.data
        user.save()
        flash('Se ha actualizado correctamente el usuario con email {}.'.format(user.email), 'success')
        # Devolvemos la vista de todos los usuarios
        return redirect(url_for('auth.get_user_all'))

@auth_bp.route('/delete_user/<user_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_user(user_id):
    user = User.get_by_id(user_id)
    if user is not None:
        email = user.email
        user.delete()
        flash('Se ha eliminado correctamente el usuario con email {}.'.format(email), 'success')
        return redirect(url_for('auth.get_user_all'))