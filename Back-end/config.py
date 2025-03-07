import os
from dotenv import load_dotenv

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "sua_chave_secreta_super_segura")
    DEBUG = True  

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/bd_bankcap'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Carrega as variáveis do .env
    load_dotenv()
    client_id = os.getenv("GOOGLE_CLIENT_ID")
    client_secret = os.getenv("GOOGLE_CLIENT_SECRET")
    redirect_uri = os.getenv("GOOGLE_REDIRECT_URI")
