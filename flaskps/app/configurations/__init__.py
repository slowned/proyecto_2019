from flask import Blueprint

configurations = Blueprint('configurations', __name__)

from . import views
