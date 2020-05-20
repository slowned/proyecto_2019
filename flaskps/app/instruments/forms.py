from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    DateField,
    SelectField,
    FileField,
)

from .constants import INSTRUMENT_TYPES

class CreateInstrumentsForm(Form):
    name = StringField('Nombre', [validators.DataRequired(message='Campo requerido')])
    type = SelectField('Tipo', [validators.DataRequired(message='Campo requerido')], choices=INSTRUMENT_TYPES)
