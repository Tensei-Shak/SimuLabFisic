from flask import Flask, redirect
from .routes.auth_routes import auth_bp
from .routes.contact_routes import contact_bp
from .routes.report_routes import report_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Registramos los Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(contact_bp, url_prefix='/contact')
    app.register_blueprint(report_bp, url_prefix='/report')    
     
    return app
