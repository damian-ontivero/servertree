"""Doc."""

from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from service.server.server import server_service


class ApplicationForm(FlaskForm):
    service_server_id = QuerySelectField("Servidor", query_factory=server_service.get_all, get_label="name")
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
