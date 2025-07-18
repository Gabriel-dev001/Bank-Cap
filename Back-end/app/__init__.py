from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config import Config
from extensions import db, jwt, migrate

from flask import jsonify

from app.routes.auth_routes import auth_bp
from app.routes.usuario_routes import usuario_bp
from app.routes.conta_routes import conta_bp
from app.routes.receita_routes import receita_bp
from app.routes.despesa_routes import despesa_bp
from app.routes.cripto_routes import cripto_bp
from app.routes.relatorio_routes import relatorio_bp

def create_app():
    app = Flask(__name__)
    app.config["JWT_SECRET_KEY"] = "sua_chave_secreta"  
    # print("JWT_SECRET_KEY:", app.config["JWT_SECRET_KEY"])
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(Config)

    # Inicializa extensões
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db) 

    # Registra Blueprints
    app.register_blueprint(usuario_bp, url_prefix="/usuarios") 
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(conta_bp, url_prefix="/contas")
    app.register_blueprint(receita_bp, url_prefix="/receitas")
    app.register_blueprint(despesa_bp, url_prefix="/despesas")
    app.register_blueprint(cripto_bp, url_prefix="/cripto")
    app.register_blueprint(relatorio_bp, url_prefix="/relatorios")

    return app
