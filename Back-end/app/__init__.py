from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, jwt, migrate

from app.routes.auth_routes import auth_bp
from app.routes.usuario_routes import usuario_bp

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)  # Gerenciador de migrações

    # Registra Blueprints
    app.register_blueprint(usuario_bp, url_prefix="/usuarios") 
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app
