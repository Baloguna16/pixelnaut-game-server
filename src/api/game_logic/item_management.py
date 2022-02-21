
from api.database import mongodriver
from .items import items
db = mongodriver.Database()

def buy_item(mint, item):
    #db.set_coin_balance(mint, 1000)
    balance = db.get_coin_balance(mint)
    price = [i['price'] for i in items if i['name'] == item][0]
    if(price > balance):
        return False
    db.set_coin_balance(mint, balance - price)
    newbalance = db.get_coin_balance(mint)
    return True