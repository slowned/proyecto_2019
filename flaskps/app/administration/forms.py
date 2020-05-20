from wtforms import (
    Form,
    StringField,
    validators,
    DateField,
    SelectField,
    IntegerField,
)

from .contants import SCHOOL_YEAR_CHOICES


class CreateSchoolYearForm(Form):
    start_date = DateField(
        'Fecha de inicio',
        [validators.DataRequired(message='Este es un campo requerido')])
    end_date = DateField(
        'Fecha de fin',
        [validators.DataRequired(message='Este es un campo requerido')])
    semester = SelectField(
        'Semestre',
        [validators.DataRequired(message='Este es un campo requerido')],
        choices=SCHOOL_YEAR_CHOICES)


class WorkshopCreateForm(Form):
    name = StringField('Nombre', [validators.DataRequired(message='Este es un campo requerido')])
    short_name = StringField('Nombre corto', [validators.DataRequired(message='Este es un campo requerido')])
    # semester = StringField('semestre', [validators.DataRequired()])
    teacher = StringField('Profesor', [validators.DataRequired(message='Este es un campo requerido')])
    nucleo = StringField('Nucleo', [validators.DataRequired(message='Este es un campo requerido')])
    address = StringField('Direccion', [validators.DataRequired(message='Este es un campo requerido')])
    horario = StringField('Horario', [validators.DataRequired(message='Este es un campo requerido')])
    days = StringField('Dia', [validators.DataRequired(message='Este es un campo requerido')])
    clases = IntegerField('Cantidad de clases', [validators.DataRequired(message='Este es un campo requerido')])
