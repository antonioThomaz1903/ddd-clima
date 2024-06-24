from dynaconf import FlaskDynaconf
from flask import Flask
import jose
from jose import jwt
from sqlalchemy import create_engine
from src.Entities import BaseUsuario
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
settings = FlaskDynaconf(app).settings

engine = create_engine(settings.DATABASE_URI)
BaseUsuario.metadata.create_all(engine)
Session_app = sessionmaker(bind=engine)
session_app = Session_app()


if __name__ == "__main__":
    from src.Services.Api import api_bp
    from src.views import web_bp

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(web_bp)
    app.run(host="127.0.0.1", port=5000)
