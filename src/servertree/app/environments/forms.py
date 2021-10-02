from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class EnvironmentForm(FlaskForm):
    environment_name = StringField('Entorno', validators=[DataRequired()])
    environment_is_active = BooleanField('Activo')