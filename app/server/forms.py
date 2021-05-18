from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length

from .models import Server, Environment, OperatingSystem, ConnectionType
class ServerForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    environment_id = QuerySelectField('Entorno', query_factory=Environment.get_all, get_label='name')
    operating_system_id = QuerySelectField('Sistema operativo', query_factory=OperatingSystem.get_all)
    cpu = StringField('CPU', validators=[DataRequired()])
    ram = StringField('RAM', validators=[DataRequired()])
    hdd = StringField('HDD', validators=[DataRequired()])
    is_active = BooleanField('Activo')

class AccessForm(FlaskForm):
    server_id = QuerySelectField('Servidor', query_factory=Server.get_all, get_label='name')
    connection_type_id = QuerySelectField('Tipo de conexión', query_factory=ConnectionType.get_all, get_label='name')
    ip_local = StringField('IP local')
    port_local = StringField('Puerto local')
    ip_public = StringField('IP pública')
    port_public = StringField('Puerto público')
    username = StringField('Usuario', validators=[DataRequired()])
    password = StringField('Contraseña', validators=[DataRequired()])
    is_active = BooleanField('Activo')

class AppForm(FlaskForm):
    server_id = QuerySelectField('Servidor', query_factory=Server.get_all, get_label='name')
    name = StringField('Nombre', validators=[DataRequired()])
    version = StringField('Versión', validators=[DataRequired()])
    arch = StringField('Arquitectura', validators=[DataRequired()])
    ip_local = StringField('IP local')
    port_local = StringField('Puerto local')
    ip_public = StringField('IP pública')
    port_public = StringField('Puerto público')
    install_dir = StringField('Directorio intalación', validators=[DataRequired()])
    log_dir = StringField('Directorio logs', validators=[DataRequired()])
    is_active = BooleanField('Activo')