import pymongo
import os
print(os.curdir)
from api.game_logic import orcanaut

class Database:
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        self.db = client.newdb
        self.mint_number = -1

    def get_name(self, name):
        print(self.db.test.find_one({'name':'matt'})['role'])

    def buy_item(name):
        return False

    def set_mint_number(self, num):
        self.mint_number = num

    def get_orcanaut():
        return orcanaut.Orcanaut()

    def get_state():
        pass

    def feed_fish():
        pass

    def clean_tank():
        pass

    def complete_mini_game(points):
        pass
