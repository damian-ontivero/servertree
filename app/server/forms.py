from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length

from .models import Server, Environment, OperatingSystem, ConnectionType
class ServerForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    environment_id = QuerySelectField('Entorno', query_factory=Environment.get_all, get_label='name', allow_blank=True, blank_text='Seleccione un entorno ...')
    operating_system_id = QuerySelectField('Sistema operativo', query_factory=OperatingSystem.get_all, allow_blank=True, blank_text='Seleccione un sistema operativo ...')
    cpu = StringField('CPU', validators=[DataRequired()])
    ram = StringField('RAM', validators=[DataRequired()])
    hdd = StringField('HDD', validators=[DataRequired()])
    is_active = BooleanField('Activo')

class AccessForm(FlaskForm):
    server_id = QuerySelectField('Servidor', query_factory=Server.get_all, get_label='name')
    connection_type_id = QuerySelectField('Tipo de conexión', query_factory=ConnectionType.get_all, get_label='name', allow_blank=True, blank_text='Seleccione un tipo de conexión ...')
    ip_local = StringField('IP local')
    port_local = StringField('Puerto local')
    ip_public = StringField('IP pública')
    port_public = StringField('Puerto público')
    username = StringField('Usuario', validators=[DataRequired()])
    password = StringField('Contraseña', validators=[DataRequired()])
    is_active = BooleanField('Activo')