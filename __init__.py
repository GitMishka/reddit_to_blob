from flask import Flask
from .routes import register_routes

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    register_routes(app)

    return app
