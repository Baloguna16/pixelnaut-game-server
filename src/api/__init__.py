from flask import Flask

def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)

    from .routes import state
    app.register_blueprints(state)

    return app
