from wtforms import Form, BooleanField, StringField, PasswordField, validators


class LogInForm(Form):
    email = StringField('Email', [
                validators.Length(min=6, max=35),
                validators.DataRequired()
            ])
    password = PasswordField('Contrasenia', [validators.DataRequired()])
