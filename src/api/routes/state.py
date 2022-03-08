from bson.json_util import dumps
from flask import Blueprint, jsonify, request, Response, session
from api.database import mongodriver
from api.game_logic.time_management import check_timeouts
from api.utils.attribute_finder import get_nft_info
import api.game_logic
bp = Blueprint('main', __name__)
db = mongodriver.Database()

@bp.route('/index')
def say_hello():
    return "hello, web3."

@bp.route('/tank/load')
def load_state():
    mint_number = request.json['mint']
    if(not mint_number):
        return jsonify("Mint number not set"), 501
    result = db.get_state(mint_number)
    check_timeouts(mint_number)
    if(result):
        result['type'] = 'load'
        return dumps(result), 200
    return jsonify("Could not get state from database"), 404

@bp.route('/coinbalance')
def get_coin_balance():
    mint_number = request.json['mint']
    if(not mint_number):
        return jsonify("Mint number not set"), 501
    result = db.get_state(mint_number)
    check_timeouts(mint_number)
    if(result):
        return dumps({'coins':result['coins'], 'type':'coinbalance'}), 200
    return jsonify("Could not get state from database"), 404

@bp.route('/upgradetank', methods = ['POST'])
def upgrade_tank():
    tank = request.json['tank']
    mint = request.json['mint']
    if(not mint):
        return jsonify("Mint number not set"), 501
    if(not tank):
        return jsonify("Need to set a tank in the json data"), 401        
    cost = api.game_logic.upgrade_tank(mint, tank)
    if cost:
        return jsonify({'type': 'upgradetank', 'result': 'success', 'cost': cost}), 200
    else:
        return jsonify({'type': 'upgradetank', 'result': 'fail'}), 200

#Need to encrypt the number of coins
@bp.route('/wingame', methods = ['POST'])
def win_game():
    mint = request.json['mint']
    coins = request.json['coins']
    if not mint:
        return jsonify("Mint number not set"), 501
    if not coins:
        return jsonify("Need to set the number of coins json data"), 401
    balance = db.get_coin_balance(mint)
    db.set_coin_balance(mint, balance + coins)   
    return jsonify({'type': 'wingame', 'result': 'success'}), 200

@bp.route('/buyitem', methods = ['POST'])
def buy_item():
    mint = request.json['mint']
    item = request.json['item']
    if not mint:
        return jsonify("Mint number not set"), 501
    if not item:
        return jsonify("Need to set an item in the json data"), 401        
    cost = api.game_logic.buy_item(mint, item)
    if cost > 0:
        return jsonify({'type': 'buyitem', 'result': 'success', 'cost': cost, 'item': item}), 200
    else:
        return jsonify({'type': 'buyitem', 'result': 'fail', 'item': item, 'cost': cost}), 200

@bp.route('/feedfish', methods=['POST'])
def feed_fish():
    mint = request.json['mint']
    if(not mint):
        return jsonify("Mint number not set"), 501
    coins = api.game_logic.feed_fish(mint)
    return jsonify({'type': 'feedfish', 'result': 'success', 'coins': coins}), 200

@bp.route('/changewater', methods=['POST'])
def change_water():
    mint = request.json['mint']
    if(not mint):
        return jsonify("Mint number not set"), 501 
    coins = api.game_logic.clean_tank(mint)
    return jsonify({'type': 'changewater', 'result': 'success', 'coins': coins}), 200


@bp.route('/update/itemposition', methods=['POST'])
def update_item_position():
    mint = request.json['mint']
    item = request.json['item']
    x = request.json['x']
    y = request.json['y']
    db.update_item_position(mint, item, x, y)
    return jsonify({'type': 'itemposition', 'result': 'success'}), 200