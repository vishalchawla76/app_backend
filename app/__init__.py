from flask import Flask, Blueprint
from .routes import main


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    return app

app1 = create_app()

app1.register_blueprint(main)
