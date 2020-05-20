from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    DateField,
    SelectField,
    IntegerField
)

import datetime

from .constants import (
    GENDER_CHOICES,
)

def validate_char(form, field):
    if any(char.isdigit() for char in field.data):
        raise validators.ValidationError('No se permiten numeros en el campo')

def validate_date(form, field):
    if field.data > datetime.date.today():
        raise validators.ValidationError('La fecha no puede ser posterior a la actual')

class CreateStudentsForm(Form):
    surname = StringField('Apellido', [validators.DataRequired(message='Este es un campo requerido'),validate_char])
    name = StringField('Nombre', [validators.DataRequired(message='Este es un campo requerido'), validate_char])
    birth_date = DateField('Fecha de nacimiento', [validators.DataRequired(message='Este es un campo requerido'), validate_date], format='%Y-%m-%d')
    borned = StringField('Lugar de nacimiento')
    locality = StringField('Localidad', [validators.DataRequired(message='Este es un campo requerido')])
    address = StringField('Direccion', [validators.DataRequired(message='Este es un campo requerido')])
    neighborhood = StringField('Barrio', [validators.DataRequired(message='Este es un campo requerido')])
    gender = SelectField('Genero', [validators.DataRequired(message='Este es un campo requerido')], choices=GENDER_CHOICES)
    document_type = StringField('Tipo de documento', [validators.DataRequired(message='Este es un campo requerido')])
    document_number = StringField('Numero de documento', [validators.DataRequired(message='Este es un campo requerido')])
    tutor = StringField('Tutor', [validators.DataRequired(message='Este es un campo requerido')])
    phone = IntegerField('Telefono', [validators.DataRequired(message='Solo se permite ingresar numeros')])
    school = StringField('Escuela', [validators.DataRequired(message='Este es un campo requerido')])
    level = StringField('Nivel', [validators.DataRequired(message='Este es un campo requerido')])
    tutor_name = StringField('Nombre del tutor', [validators.DataRequired(message='Este es un campo requerido')])
