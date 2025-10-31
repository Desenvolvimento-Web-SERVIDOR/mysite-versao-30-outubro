from flask import Blueprint

main = Blueprint('main', __name__)

# Importa views e errors no final para evitar 'circular imports'
from . import views, errors
