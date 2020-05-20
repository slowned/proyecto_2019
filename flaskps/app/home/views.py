from flask import render_template
from flask_login import login_required
from flaskps.app.configurations.models import Configurations

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    check if home is available
    """
    conf = Configurations.query.first()
    if conf.active:
        return render_template('home/index.html', conf=conf)
    return render_template('home/fuera_de_servicio.html', conf=conf)

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")
