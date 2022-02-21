
from api.database import mongodriver
from .items import items
from .items import tanks
db = mongodriver.Database()


def upgrade_tank(mint, tank):
    balance = db.get_coin_balance(mint)
    price = [i['price'] for i in tanks if i['name'] == tank][0]
    if(price > balance):
        return False
    result = db.get_state(mint)
    if tank == result["tank"]["type"]:
        return False 
    db.set_coin_balance(mint, balance - price)
    db.switch_tank(mint, tank)
    result = db.get_state(mint)

    return True
def buy_item(mint, item):
    #db.set_coin_balance(mint, 1000)
    balance = db.get_coin_balance(mint)
    price = [i['price'] for i in items if i['name'] == item][0]
    if(price > balance):
        return False
    result = db.get_state(mint)
    if item in result["tank"]["decorations"]:
        return False 
    db.set_coin_balance(mint, balance - price)
    db.add_item(mint, item)
    result = db.get_state(mint)
    return True