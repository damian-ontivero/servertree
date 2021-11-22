"""Doc."""

from flask_wtf import FlaskForm

from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class ConnectionTypeForm(FlaskForm):
    connection_type_name = StringField("Tipo de conexión", validators=[DataRequired()])
    connection_type_is_active = BooleanField("Activo")
