"""Doc."""

from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from service.server.server import ServerService
from service.connection_type.connection_type import ConnectionTypeService


class AccessForm(FlaskForm):
    access_server_id = QuerySelectField("Servidor", query_factory=ServerService.get_all, get_label="name")
    access_connection_type_id = QuerySelectField("Tipo de conexión", query_factory=ConnectionTypeService.get_all, get_label="name")
    access_ip_local = StringField("IP local")
    access_port_local = StringField("Puerto local")
    access_ip_public = StringField("IP pública")
    access_port_public = StringField("Puerto público")
    access_username = StringField("Usuario", validators=[DataRequired()])
    access_password = StringField("Contraseña", validators=[DataRequired()])
    access_is_active = BooleanField("Activo")
