from crypt import methods
from bson.json_util import dumps
from urllib import response
from flask import Blueprint, jsonify, request, Response, session
from api.database import mongodriver
from api.utils.attribute_finder import get_nft_info
import api.game_logic
bp = Blueprint('main', __name__)
db = mongodriver.Database()


@bp.route('/index')
def say_hello():
    return "hello, web3."

@bp.route('/setmint')
def set_mint():
    mint_number = request.json['mint_number']
    session['mint_number'] = mint_number
    return Response(status=200)


@bp.route('/tank/load')
def load_state():
    mint_number = session.get('mint_number')
    if(not mint_number):
        return jsonify("Mint number not set"), 501
    result = db.get_state(mint_number)
    if(result):
        return dumps(result), 200
    return jsonify("Could not get state from database"), 404

@bp.route('/buyitem', methods = ['POST'])

def buy_item():
    mint = session.get('mint_number')
    item = request.json['item']
    if(not mint):
        return jsonify("Mint number not set"), 501
    if(not item):
        return jsonify("Need to set an item in the json data"), 401        
    if api.game_logic.buy_item(mint, item):
        return jsonify("success"), 200
    else:
        return jsonify("fail"), 200

@bp.route('/tank/save')
def save_state():
    data = request.json
    print(data)
    return
