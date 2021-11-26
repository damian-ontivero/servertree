"""Doc."""

from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from service.environment.environment import EnvironmentService
from service.operating_system.operating_system import OperatingSystemService
from service.environment.environment import EnvironmentService


class ServerForm(FlaskForm):
    server_name = StringField("Nombre", validators=[DataRequired()])
    server_environment_id = QuerySelectField("Entorno", query_factory=EnvironmentService.get_all, get_label="name")
    server_operating_system_id = QuerySelectField("Sistema operativo", query_factory=OperatingSystemService.get_all)
    server_cpu = StringField("CPU", validators=[DataRequired()])
    server_ram = StringField("RAM", validators=[DataRequired()])
    server_hdd = StringField("HDD", validators=[DataRequired()])
    server_is_active = BooleanField("Activo")
