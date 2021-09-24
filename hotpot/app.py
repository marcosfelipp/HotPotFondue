from flask import Flask, config
from hotpot.ext import appearance, configuration


def create_app():
    app = Flask(__name__)
    configuration.init_app(app)
    configuration.load_extensions(app)
    return app
