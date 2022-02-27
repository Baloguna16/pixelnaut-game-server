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
        return dumps(result), 200
    return jsonify("Could not get state from database"), 404

@bp.route('/upgradetank', methods = ['POST'])
def upgrade_tank():
    tank = request.json['tank']
    mint = request.json['mint']
    if(not mint):
        return jsonify("Mint number not set"), 501
    if(not tank):
        return jsonify("Need to set a tank in the json data"), 401        
    if api.game_logic.upgrade_tank(mint, tank):
        return jsonify("success"), 200
    else:
        return jsonify("fail"), 200

#Need to encrypt the number of coins
@bp.route('/wingame', methods = ['POST'])
def win_game():
    mint = request.json['mint']
    coins = request.json['coins']
    if(not mint):
        return jsonify("Mint number not set"), 501
    if(not coins):
        return jsonify("Need to set the number of coins json data"), 401
    balance = db.get_coin_balance(mint)
    db.set_coin_balance(mint, balance + coins)   
    return jsonify("success"), 200

@bp.route('/buyitem', methods = ['POST'])
def buy_item():
    mint = request.json['mint']
    item = request.json['item']
    if(not mint):
        return jsonify("Mint number not set"), 501
    if(not item):
        return jsonify("Need to set an item in the json data"), 401        
    if api.game_logic.buy_item(mint, item):
        return jsonify("success"), 200
    else:
        return jsonify("fail"), 200

@bp.route('/feedfish', methods=['POST'])
def feed_fish():
    mint = request.json['mint']
    if(not mint):
        return jsonify("Mint number not set"), 501
    api.game_logic.feed_fish(mint)
    return jsonify("success"), 200

@bp.route('/changewater', methods=['POST'])
def change_water():
    mint = request.json['mint']
    if(not mint):
        return jsonify("Mint number not set"), 501 
    api.game_logic.clean_tank(mint)
    return jsonify("success"), 200


@bp.route('/update/itemposition', methods=['POST'])
def update_item_position():
    mint = request.json['mint']
    item = request.json['item']
    x = request.json['x']
    y = request.json['y']
    db.update_item_position(mint, item, x, y)
    return jsonify("success"), 200