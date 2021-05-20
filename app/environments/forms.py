from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class EnvironmentForm(FlaskForm):
    name = StringField('Entorno', validators=[DataRequired()])
    is_active = BooleanField('Activo')