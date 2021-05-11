from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length

from .models import Environment, OperatingSystem

class AddServerForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message='Este campo es requerido ...'), Length(max=50)])
    environment_id = QuerySelectField('Entorno', query_factory=Environment.get_all, get_label='name', allow_blank=True, blank_text='Seleccione un entorno ...')
    operating_system_id = QuerySelectField('Sistema operativo', query_factory=OperatingSystem.get_all, allow_blank=True, blank_text='Seleccione un sistema operativo ...')
    cpu = StringField('CPU', validators=[DataRequired(message='Este campo es requerido ...'), Length(max=50)])
    ram = StringField('RAM', validators=[DataRequired(message='Este campo es requerido ...'), Length(max=50)])
    hdd = StringField('HDD', validators=[DataRequired(message='Este campo es requerido ...'), Length(max=50)])
    submit = SubmitField('Agregar')

class EditServerForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(message='Este campo es requerido ...'), Length(max=50)])
    environment_id = QuerySelectField('Entorno', query_factory=Environment.get_all, get_label='name', allow_blank=True, blank_text='Seleccione un entorno ...')
    operating_system_id = QuerySelectField('Sistema operativo', query_factory=OperatingSystem.get_all, allow_blank=True, blank_text='Seleccione un sistema operativo ...')
    cpu = StringField('CPU', validators=[DataRequired(message='Este campo es requerido ...'), Length(max=50)])
    ram = StringField('RAM', validators=[DataRequired(message='Este campo es requerido ...'), Length(max=50)])
    hdd = StringField('HDD', validators=[DataRequired(message='Este campo es requerido ...'), Length(max=50)])
    is_active = BooleanField('Activo')
    submit = SubmitField('Guardar')