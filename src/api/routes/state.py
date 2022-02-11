from flask import Blueprint, request

bp = Blueprint('main', __name__)

@bp.post('/index')
def say_hello():
    return "hello"

@bp.post('/tank/load')
def load_state():
    return


@bp.post('/tank/save')
def save_state():
    return
