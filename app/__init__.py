from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

# Note: Não inicializamos 'mail' (Flask-Mail) pois usamos SendGrid
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    
    # Carrega as configurações do config.py
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Inicializa as extensões
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # Registra o Blueprint 'main'
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
