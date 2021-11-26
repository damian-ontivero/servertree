"""Doc."""

from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from service.server.server import ServerService
from service.environment.environment import EnvironmentService
from service.operating_system.operating_system import OperatingSystemService
from service.connection_type.connection_type import ConnectionTypeService
from service.environment.environment import EnvironmentService


class ServerForm(FlaskForm):
    server_name = StringField("Nombre", validators=[DataRequired()])
    server_environment_id = QuerySelectField("Entorno", query_factory=EnvironmentService.get_all, get_label="name")
    server_operating_system_id = QuerySelectField("Sistema operativo", query_factory=OperatingSystemService.get_all)
    server_cpu = StringField("CPU", validators=[DataRequired()])
    server_ram = StringField("RAM", validators=[DataRequired()])
    server_hdd = StringField("HDD", validators=[DataRequired()])
    server_is_active = BooleanField("Activo")


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


class ServiceForm(FlaskForm):
    service_server_id = QuerySelectField("Servidor", query_factory=ServerService.get_all, get_label="name")
    service = StringField("Servicio", validators=[DataRequired()])
    service_version = StringField("Versión", validators=[DataRequired()])
    service_architect = StringField("Arquitectura", validators=[DataRequired()])
    service_ip_local = StringField("IP local")
    service_port_local = StringField("Puerto local")
    service_ip_public = StringField("IP pública")
    service_port_public = StringField("Puerto público")
    service_install_dir = StringField("Directorio intalación", validators=[DataRequired()])
    service_log_dir = StringField("Directorio logs", validators=[DataRequired()])
    service_is_active = BooleanField("Activo")
