"""Doc."""

from flask import (
    Flask,
    render_template,
    flash,
    request
)
from flask_login import LoginManager

from configparser import ConfigParser

from werkzeug.utils import redirect

from service.auth.user import UserService

from app.servertree.index import index_bp
from app.servertree.auth import auth_bp
from app.servertree.server import server_bp
from app.servertree.connection_type import connection_type_bp
from app.servertree.environment import environment_bp
from app.servertree.operating_system import operating_system_bp

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: int):
    """Doc."""
    return UserService.get(id=user_id)


def create_app():
    """Doc."""
    app = Flask(__name__, template_folder="servertree/templates", static_folder="servertree/static")

    config = ConfigParser()
    config_file = "./config.ini"
    config.read(filenames=config_file)

    app.config["SECRET_KEY"] = config.get("flask", "SECRET_KEY")

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Inicie sesión para acceder a la página."
    login_manager.login_message_category = "warning"

    # Registro de los Blueprint creado
    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(server_bp)
    app.register_blueprint(connection_type_bp)
    app.register_blueprint(environment_bp)
    app.register_blueprint(operating_system_bp)

    # Custom error handlers
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    """Doc."""
    @app.errorhandler(500)
    def base_error_handler(e):
        """Doc."""
        return render_template("500.html"), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        """Doc."""
        return render_template("404.html"), 404

    @app.errorhandler(401)
    def error_401_handler(e):
        """Doc."""
        return render_template("401.html"), 401

    @app.errorhandler(IntegrityError)
    def error_integrity_handler(e):
        """Doc."""
        flash("El email ya está registrado por otro usuario.", "danger")
        return redirect(request.referrer)

    @app.errorhandler(UnmappedInstanceError)
    def error_unmapped_instance_handler(e):
        """Doc."""
        return render_template("404.html"), 404
