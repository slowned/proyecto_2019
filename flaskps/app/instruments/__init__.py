from flask import Blueprint
instruments = Blueprint('instruments', __name__)
from . import views
