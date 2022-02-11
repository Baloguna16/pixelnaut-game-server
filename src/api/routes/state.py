from flask import Blueprint, request

bp = Blueprint('main', __name__)

@bp.route('/index')
def say_hello():
    return "hello, web3."


@bp.route('/tank/load')
def load_state():
    data = request.json
    print(data)
    return


@bp.route('/tank/save')
def save_state():
    data = request.json
    print(data)
    return
