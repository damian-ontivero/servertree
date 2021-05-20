from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired, Length

class OperatingSystemForm(FlaskForm):
    name = StringField('Sistema operativo', validators=[DataRequired()])
    version = StringField('Versión', validators=[DataRequired()])
    architect = StringField('Arquitectura', validators=[DataRequired(), Length(max=6)])