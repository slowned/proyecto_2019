from wtforms import (
    Form,
    BooleanField,
    StringField,
    PasswordField,
    validators,
    SelectField,
)

def validate_char(form, field):
    if any(char.isdigit() for char in field.data):
        raise validators.ValidationError('No se permiten numeros en el campo')

class CreateFormUser(Form):
    email = StringField('Email', [validators.Email(), validators.InputRequired(message='Campo requerido')])
    username = StringField('Nombre de usuario', [validators.InputRequired(message='Campo requerido')])
    name =StringField('Nombre', [validators.InputRequired(message='Campo requerido'),validate_char])
    surname = StringField('Apellido', [validators.InputRequired(message='Campo requerido'),validate_char])
    password = StringField('Password', [validators.InputRequired(message='Campo requerido')])
    active = BooleanField('Activo')
    roles = StringField('Roles',[validators.InputRequired(message='Campo requerido')])
