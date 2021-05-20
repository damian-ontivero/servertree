from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class ConnectionType(FlaskForm):
    name = StringField('Tipo de conexión', validators=[DataRequired()])
    is_active = BooleanField('Activo')