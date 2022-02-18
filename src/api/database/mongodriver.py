from datetime import datetime
import pymongo
import os
from datetime import datetime
print(os.curdir)
from api.game_logic import orcanaut

class Database:
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        self.db = client.newdb
        a = {'a' : {1:2,3:4}}

    def get_name(self, name):
        print(self.db.test.find_one({'name':'matt'})['role'])

    def buy_item(name):
        return False

    def initialize_orcanaut(self, num):
        doc = {'mint_number': num, 
            'orcanaut': {
                'attributes' : {
                    'eyes': '',
                    'accessory':'',
                    'hat':'',
                    'mouth':'',
                    'background':'',
                },
                'stats':{
                    'cute': 0,
                    'speed': 0,
                    'social': 0,
                    'nimble': 0,
                    'wealthy': 0
                },
                'coins': 0
            },
            'tank' : {
                'last_cleaned': datetime.timestamp(datetime.now()),
                'last_fed': datetime.timestamp(datetime.now()),
                'decorations': [],
                'type': 'bag' 
            }}
        self.db.pixelpets.insert_one(doc)

    def get_orcanaut(self):
        return orcanaut.Orcanaut()

    def get_state(self,mint_number):
        result = self.db.pixelpets.find_one({'mint_number' : mint_number})
        if(result == None):
            self.initialize_orcanaut(mint_number)
            result = self.db.pixelpets.find_one({'mint_number' : mint_number})
        return result


    def feed_fish(self):
        pass

    def clean_tank(self):
        pass

    def complete_mini_game(self, points):
        pass
