"""Doc."""

from flask import (
    render_template,
    redirect,
    request,
    url_for,
    jsonify,
    flash
)
from flask_login import (
    current_user,
    login_user,
    login_required,
    logout_user
)

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.urls import url_parse

from app.servertree.auth import auth_bp
from app.servertree.auth.forms import LoginForm, UserForm
from app.servertree.auth.decorators import admin_required
from model.auth.user import UserModel
from model.environment.environment import EnvironmentModel
from service.auth.user import UserService


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index.index"))

    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = login_form.email.data
        user = UserService.get_by_email(email=email)

        if user and check_password_hash(user.password, login_form.password.data) and user.is_active:
            login_user(user, remember=login_form.remember_me.data)
            flash(f"Se ha iniciado sesión correctamente con el usuario {email}.", "success")

            next_page = request.args.get("next")
            if not next_page or url_parse(next_page).netloc != "":
                next_page = url_for("index.index")

            return redirect(next_page)
        elif not user or not check_password_hash(user.password, login_form.password.data):
            flash("Email o contraseña incorrecto.", "danger")
        elif not user.is_active:
            flash("Usuario inactivo.", "danger")

    return render_template("login.html", login_form=login_form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth_bp.route("/get_all", methods=["GET", "POST"])
@login_required
def get_all():
    user_list = UserService.get_all()
    environment_list = EnvironmentModel.get_all()
    user_form = UserForm()
    return render_template(
        "user.html",
        user_list=user_list,
        environment_list=environment_list,
        user_form=user_form
    )


@auth_bp.route("/get/<int:user_id>", methods=["GET", "POST"])
@login_required
def get(user_id: int):
    user = UserService.get_by_id(user_id)
    return jsonify(
        firstname=user.firstname,
        lastname=user.lastname,
        email=user.email,
        password=user.password,
        role_id=user.role_id,
        is_active=user.is_active
    )


@auth_bp.route("/add", methods=["GET", "POST"])
@login_required
@admin_required
def add():
    """Doc."""
    user_form = UserForm()

    if user_form.validate_on_submit():
        # Creamos el usuario y lo guardamos
        user = UserModel(
            firstname=user_form.firstname.data,
            lastname=user_form.lastname.data,
            email=user_form.email.data,
            password=generate_password_hash(user_form.password.data),
            role_id=user_form.role_id.data.id,
            is_active=user_form.is_active.data
        )

        UserService.add(user=user)

        flash(f"Se ha registrado correctamente el usuario con email {user.email}.", "success")

    # Devolvemos la vista de todos los usuarios
    return redirect(url_for("auth.get_all"))


@auth_bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
@login_required
def edit(user_id: int):
    """Doc."""
    user = UserService.get_by_id(id=user_id)
    user_form = UserForm(obj=user)

    if user_form.validate_on_submit():
        # Recuperamos los datos del formulario
        user.firstname = user_form.firstname.data
        user.lastname = user_form.lastname.data
        user.email = user_form.email.data
        # Importante! Se accede a "...data.id" porque desde el campo "QuerySelectField"
        # llega el objeto completo y debemos acceder a la propiedad "id"
        user.role_id = user_form.role_id.data.id
        user.is_active = user_form.is_active.data

        if user_form.change_password.data:
            user.password = generate_password_hash(user_form.password.data)

        UserService.edit(user=user)

        flash(f"Se ha actualizado correctamente el usuario con email {user_form.email.data}.", "success")

    # Devolvemos la vista de todos los usuarios
    return redirect(url_for("auth.get_all"))


@auth_bp.route("/delete/<int:user_id>", methods=["GET", "POST"])
@login_required
@admin_required
def delete(user_id: int):
    user = UserService.get_by_id(id=user_id)

    UserService.delete(user=user)

    flash(f"Se ha eliminado correctamente el usuario con email {user.email}.", "success")

    # Devolvemos la vista de todos los usuarios
    return redirect(url_for("auth.get_all"))
