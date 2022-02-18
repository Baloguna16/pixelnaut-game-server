from flask import Blueprint, jsonify, request, Response
from api.database import mongodriver
bp = Blueprint('main', __name__)
db = mongodriver.Database()
is_mint_set = False

@bp.route('/index')
def say_hello():
    return "hello, web3."

@bp.route('/setmint')
def set_mint():
    mint_number = int(request.json['mint_number'])
    if(mint_number and mint_number > 0 and mint_number < 10000):
        is_mint_set = True
        return Response(status=200)
    else:
        return jsonify("Invalid mint number"), 501

@bp.route('/tank/load')
def load_state():
    if(not is_mint_set):
        return jsonify("Mint number not set"), 501
    return Response(status=200, data=db.get_state())


@bp.route('/tank/save')
def save_state():
    data = request.json
    print(data)
    return
