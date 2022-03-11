from api.database import mongodriver
from .items import items
from .items import tanks
db = mongodriver.Database()


def upgrade_tank(mint, tank):
    balance = db.get_coin_balance(mint)
    price = [i['price'] for i in tanks if i['name'] == tank][0]
    if(price > balance):
        return 0, balance
    result = db.get_state(mint)
    if tank == result["tank"]["type"]:
        return -1, balance 
    db.set_coin_balance(mint, balance - price)
    db.switch_tank(mint, tank)
    result = db.get_state(mint)
    return price, balance - price

    return True
def buy_item(mint, item):
    #db.set_coin_balance(mint, 1000)
    balance = db.get_coin_balance(mint)
    price = [i['price'] for i in items if i['name'] == item][0]
    if(price > balance):
        return 0, balance
    result = db.get_state(mint)
    if item in [x['item'] for x in result['tank']['decorations']]:
        return -1, balance
    db.set_coin_balance(mint, balance - price)
    db.add_item(mint, item)
    return price, balance - price