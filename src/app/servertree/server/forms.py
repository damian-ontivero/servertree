"""Doc."""

from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from service.operating_system.operating_system import operating_system_service
from service.environment.environment import environment_service


class ServerForm(FlaskForm):
    server_name = StringField("Nombre", validators=[DataRequired()])
    server_environment_id = QuerySelectField("Entorno", query_factory=environment_service.get_all, get_label="name")
    server_operating_system_id = QuerySelectField("Sistema operativo", query_factory=operating_system_service.get_all)
    server_cpu = StringField("CPU", validators=[DataRequired()])
    server_ram = StringField("RAM", validators=[DataRequired()])
    server_hdd = StringField("HDD", validators=[DataRequired()])
    server_is_active = BooleanField("Activo")
