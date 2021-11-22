"""Doc."""

from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from model.auth.role import RoleModel


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    remember_me = BooleanField("Recuérdame")


class UserForm(FlaskForm):
    firstname = StringField("Nombre", validators=[DataRequired()])
    lastname = StringField("Apellido", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    change_password = BooleanField("Cambiar contraseña")
    password = PasswordField("Contraseña", validators=[DataRequired()])
    show_password = BooleanField("Mostrar contraseña")
    role_id = QuerySelectField("Rol", query_factory=RoleModel.get_all, get_label="role")
    is_active = BooleanField("Activo")
