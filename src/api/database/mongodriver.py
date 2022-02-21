from datetime import datetime
import pymongo
import os
from datetime import datetime
from api.utils.default_chars import get_default_stats

from api.utils.attribute_finder import get_nft_info
print(os.curdir)

class Database:
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        self.db = client.newdb
        a = {'a' : {1:2,3:4}}

    def get_name(self, name):
        print(self.db.test.find_one({'name':'matt'})['role'])

    def initialize_orcanaut(self, num):
        orcanaut = get_nft_info(num)
        stats = get_default_stats(orcanaut)
        doc = {'mint_number': num, 
            'orcanaut': {
                'attributes' : orcanaut,
                'stats':stats,
                'coins': 0
            },
            'tank' : {
                'last_cleaned': datetime.timestamp(datetime.now()),
                'last_fed': datetime.timestamp(datetime.now()),
                'decorations': [],
                'type': 'bag' 
            }}
        self.db.pixelpets.insert_one(doc)
    
    def get_coin_balance(self, mint):
        state = self.get_state(mint)
        return state['orcanaut']['coins']

    def set_coin_balance(self, mint, balance):
        result = self.db.pixelpets.update_one({'mint_number': mint}, {'$set': {'orcanaut.coins': balance}})
        a = 1

    def get_state(self,mint):
        result = self.db.pixelpets.find_one({'mint_number' : mint})
        if(result == None):
            self.initialize_orcanaut(mint)
            result = self.db.pixelpets.find_one({'mint_number' : mint})
        return result


    def feed_fish(self):
        pass

    def clean_tank(self):
        pass

    def complete_mini_game(self, points):
        pass




