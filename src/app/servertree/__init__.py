"""Doc."""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from configparser import ConfigParser

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
config = ConfigParser()
config_file = './config.ini'


def create_app():
    app = Flask(__name__)

    config.read(filenames=config_file)

    app.config['SECRET_KEY'] = config.get('flask', 'SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get('flask-sqlalchemy', 'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.get('flask-sqlalchemy', 'SQLALCHEMY_TRACK_MODIFICATIONS')
    app.config['JSON_SORT_KEYS'] = config.get('flask-sqlalchemy', 'JSON_SORT_KEYS')

    db.init_app(app)
    migrate.init_app(app, db)
    """
    flask db init: Crea una estructura de directorios y ficheros necesarios para la ejecución de esta extensión.
                   Se ejecuta solo una vez, al principio.
    flask db migrate: Navega entre los modelos en busca de actualizaciones y genera los ficheros de migración
                      de base de datos con los cambios detectados.
    flask db upgrade: Lleva a cabo la migración de la base de datos.
    """

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Inicie sesión para acceder a la página.'
    login_manager.login_message_category = "warning"
    Bootstrap(app)

    # Registro de los Blueprint creado
    from .index import index_bp
    app.register_blueprint(index_bp)

    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .server import server_bp
    app.register_blueprint(server_bp)

    from .connection_type import connection_type_bp
    app.register_blueprint(connection_type_bp)

    from .environments import environment_bp
    app.register_blueprint(environment_bp)

    from .operating_systems import operating_system_bp
    app.register_blueprint(operating_system_bp)

    # Custom error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404

    @app.errorhandler(401)
    def error_401_handler(e):
        return render_template('401.html'), 401
