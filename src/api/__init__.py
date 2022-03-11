from flask import Flask
from flask_cors import CORS

from .utils import Config
from .database import Database

def create_app(config_object=Config()):

    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_object)
    app.secret_key = "this is my key"
    from .routes import state
    app.register_blueprint(state)
    db = Database()
    db.get_name('matt')

    return app
