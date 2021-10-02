"""Docs."""

from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length


class OperatingSystemForm(FlaskForm):
    operating_system_name = StringField('Sistema operativo', validators=[DataRequired()])
    operating_system_version = StringField('Versión', validators=[DataRequired()])
    operating_system_architect = StringField('Arquitectura', validators=[DataRequired(), Length(max=6)])
    operating_system_is_active = BooleanField('Activo')
