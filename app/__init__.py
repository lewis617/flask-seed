from flask import Flask
from config import config
from jac.contrib.flask import JAC


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    jac = JAC(app)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
