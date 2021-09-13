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
from app.environments.models import Environment




@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index.index'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        user = User.get_by_email(email)
        if user is not None and user.check_password(login_form.password.data) and user.is_active:
            login_user(user, remember=login_form.remember_me.data)
            flash('Se ha iniciado sesión correctamente con el usuario {}.'.format(email), 'success')
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index.index')
            return redirect(next_page)
        elif user is None or not user.check_password(login_form.password.data):
            flash('Email o contraseña incorrecto.', 'danger')
        elif not user.is_active:
            flash('Usuario inactivo.', 'danger')

    return render_template('login.html', login_form=login_form)

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
    environments = Environment.get_all()
    user_form = UserForm()
    return render_template('user.html', data=data, environments=environments, user_form=user_form)

@auth_bp.route('/get_user', methods=['GET', 'POST'])
@login_required
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
    user_form = UserForm()
    if user_form.validate_on_submit():
        # Recuperamos los datos del formulario
        firstname = user_form.firstname.data
        lastname = user_form.lastname.data
        email = user_form.email.data
        password = user_form.password.data
        # Importante! Se accede a '...data.id' porque desde el campo 'QuerySelectField'
        # llega el objeto completo y debemos acceder a la propiedad 'id'
        role_id = user_form.role_id.data.id
        is_active = user_form.is_active.data
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
    return redirect(request.referrer)

@auth_bp.route('/edit_user/<user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    user = User.get_by_id(user_id)
    user_form = UserForm(obj=user)
    if user_form.validate_on_submit():
        if user.email == user_form.email.data:
            # Recuperamos los datos del formulario
            user.firstname = user_form.firstname.data
            user.lastname = user_form.lastname.data
            user.email = user_form.email.data
            # Importante! Se accede a '...data.id' porque desde el campo 'QuerySelectField'
            # llega el objeto completo y debemos acceder a la propiedad 'id'
            user.role_id = user_form.role_id.data.id
            user.is_active = user_form.is_active.data
            if user_form.change_password.data:
                user.set_password(user_form.password.data)
            user.save()
            flash('Se ha actualizado correctamente el usuario con email {}.'.format(user_form.email.data), 'success')
        else: 
            if User.get_by_email(user_form.email.data) is not None:
                flash('El email {} ya está registrado por otro usuario.'.format(user_form.email.data), 'danger')
            else:
                # Recuperamos los datos del formulario
                user.firstname = user_form.firstname.data
                user.lastname = user_form.lastname.data
                user.email = user_form.email.data
                # Importante! Se accede a '...data.id' porque desde el campo 'QuerySelectField'
                # llega el objeto completo y debemos acceder a la propiedad 'id'
                user.role_id = user_form.role_id.data.id
                user.is_active = user_form.is_active.data
                if user_form.change_password.data:
                    user.set_password(user_form.password.data)
                user.save()
                flash('Se ha actualizado correctamente el usuario con email {}.'.format(user_form.email.data), 'success')
    # Devolvemos la vista de todos los usuarios
    return redirect(request.referrer)

@auth_bp.route('/delete_user/<user_id>', methods=['GET', 'POST'])
@login_required
@admin_required
def delete_user(user_id):
    user = User.get_by_id(user_id)
    if user is not None:
        email = user.email
        user.delete()
        flash('Se ha eliminado correctamente el usuario con email {}.'.format(email), 'success')
        return redirect(request.referrer)