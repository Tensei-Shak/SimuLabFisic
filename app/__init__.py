from flask import Flask
from .routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Registramos los Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
