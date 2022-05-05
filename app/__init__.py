from flask import Flask
from app.config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name) or "development")
    return app