from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length

from .models import Environment, OperatingSystem
class ServerForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    environment_id = QuerySelectField('Entorno', query_factory=Environment.get_all, get_label='name', allow_blank=True, blank_text='Seleccione un entorno ...')
    operating_system_id = QuerySelectField('Sistema operativo', query_factory=OperatingSystem.get_all, allow_blank=True, blank_text='Seleccione un sistema operativo ...')
    cpu = StringField('CPU', validators=[DataRequired()])
    ram = StringField('RAM', validators=[DataRequired()])
    hdd = StringField('HDD', validators=[DataRequired()])
    is_active = BooleanField('Activo')