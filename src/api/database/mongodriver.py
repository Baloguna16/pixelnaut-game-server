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

    def get_orcanaut(self):
        return orcanaut.Orcanaut()

    def get_state(self,mint_number):
        result = self.db.pixelpets.find_one({'mint_number' : mint_number})
        return result


    def feed_fish(self):
        pass

    def clean_tank(self):
        pass

    def complete_mini_game(self, points):
        pass
