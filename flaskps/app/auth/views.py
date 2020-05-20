from flask import render_template, redirect, request, flash
from flask_login import login_required, login_manager, login_user, logout_user

from flaskps.app.users.models import User
from flaskps.app.auth.forms import LogInForm

from . import auth


@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    """
    Muestra el template de login
    """
    form = LogInForm(request.form)
    if request.method == 'POST' and form.validate():
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user.verify_password(password):
            login_user(user)
            return redirect('/dashboard')
        flash('Verificar usuario o contrasenia')
    return render_template('auth/login.html', title="login")

@auth.route('/auth/logout')
@login_required
def logout():
    logout_user()
    return render_template('auth/login.html')
