from flask import Blueprint
from app.controllers.auth_controller import AuthController

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

auth_bp.route("/register", methods=["POST"])(AuthController.registrar)
auth_bp.route("/login", methods=["POST"])(AuthController.login)
auth_bp.route("/trocar-senha/<int:usuario_id>", methods=["PUT"])(AuthController.trocar_senha)
auth_bp.route("/google/login", methods=["POST"])(AuthController.login_com_google)
auth_bp.route("/google/register", methods=["POST"])(AuthController.registrar_com_google)
auth_bp.route("/google/callback", methods=["GET"])(AuthController.callback_google)