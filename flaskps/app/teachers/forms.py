from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    DateField,
    SelectField,
    IntegerField,
)

import datetime

def validate_char(form, field):
    if any(char.isdigit() for char in field.data):
        raise validators.ValidationError('No se permiten numeros en el campo')

def validate_date(form, field):
    if field.data > datetime.date.today():
        raise validators.ValidationError('La fecha no puede ser posterior a la actual')

class CreateTeachersForm(Form):
    surname = StringField('Apellido', [validators.DataRequired(message='Este es un campo requerido'), validate_char])
    name = StringField('Nombre', [validators.DataRequired(message='Este es un campo requerido'), validate_char])
    birth_date = DateField('Fecha de nacimiento', [validators.DataRequired(message='Este es un campo requerido'), validate_date], format='%Y-%m-%d')
    locality = StringField('Localidad', [validators.DataRequired(message='Este es un campo requerido')])
    address = StringField('Direccion', [validators.DataRequired(message='Este es un campo requerido')])
    document_type = SelectField('Tipo de documento', choices=[('DNI', 'DNI'), ('LC', 'LC'), ('LE', 'LE'), ('Pasaporte', 'Pasaporte')])
    document_number = StringField('Numero de documento', [validators.DataRequired(message='Este es un campo requerido')])
    phone = IntegerField('Telefono', [validators.DataRequired(message='Solo se permite ingresar numeros')])
