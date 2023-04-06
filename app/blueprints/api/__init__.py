from flask import Blueprint
# Create a blueprint instance
api = Blueprint('api', __name__, url_prefix='/api')

from . import routes