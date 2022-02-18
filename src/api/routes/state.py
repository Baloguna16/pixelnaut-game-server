from bson.json_util import dumps
from urllib import response
from flask import Blueprint, jsonify, request, Response, session
from api.database import mongodriver
bp = Blueprint('main', __name__)
db = mongodriver.Database()


@bp.route('/index')
def say_hello():
    return "hello, web3."

@bp.route('/setmint')
def set_mint():
    mint_number = int(request.json['mint_number'])
    if(mint_number and mint_number > 0 and mint_number < 10000):
        session['mint_number'] = mint_number
        return Response(status=200)
    else:
        return jsonify("Invalid mint number"), 501

@bp.route('/tank/load')
def load_state():
    mint_number = session.get('mint_number')
    if(not mint_number):
        return jsonify("Mint number not set"), 501
    result = db.get_state(mint_number)
    if(result):
        return dumps(result), 200
    return jsonify("Could not get state from database"), 404

@bp.route('/tank/save')
def save_state():
    data = request.json
    print(data)
    return
