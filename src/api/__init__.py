from flask import Flask

from .utils import Config
from .database import Database

def create_app(config_object=Config()):

    app = Flask(__name__)
    app.config.from_object(config_object)

    from .routes import state
    app.register_blueprint(state)
    db = Database()
    db.get_name('matt')

    return app
