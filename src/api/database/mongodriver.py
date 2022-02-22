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
            'coins': 0,
            'orcanaut': {
                'attributes' : orcanaut,
                'stats':stats,
                'last_fed': datetime.timestamp(datetime.now())
            },
            'tank' : {
                'last_cleaned': datetime.timestamp(datetime.now()),
                'decorations': [],
                'type': 'bag' 
            }}
        self.db.pixelpets.insert_one(doc)
    
    def get_coin_balance(self, mint):
        state = self.get_state(mint)
        return state['coins']

    def set_coin_balance(self, mint, balance):
        result = self.db.pixelpets.update_one({'mint_number': mint}, {'$set': {'coins': balance}})

    def switch_tank(self, mint, tank):
        result = self.db.pixelpets.update_one({'mint_number': mint}, {'$set': {'tank.type': tank}})

    def add_item(self, mint, item):
        result = self.db.pixelpets.update_one({'mint_number': mint}, {'$push': {'tank.decorations': item}})

    def get_state(self,mint):
        result = self.db.pixelpets.find_one({'mint_number' : mint})
        if(result == None):
            self.initialize_orcanaut(mint)
            result = self.db.pixelpets.find_one({'mint_number' : mint})
        return result


    def feed_fish(self, mint):
        result = self.db.pixelpets.update_one({'mint_number': mint},{'$set':{'orcanaut.last_fed':datetime.timestamp(datetime.now())}})

    def clean_tank(self, mint):
        result = self.db.pixelpets.update_one({'mint_number': mint},{'$set':{'tank.last_cleaned':datetime.timestamp(datetime.now())}})

    def reset_stats(self,mint):
        orcanaut = self.db.pixelpets.find_one({'mint_number': mint})['orcanaut']['attributes']
        stats = get_default_stats(orcanaut)
        result = self.db.pixelpets.update_one({'mint_number': mint}, {'$set':{'orcanaut.stats': stats}})

    def increase_stats(self,mint,increase):
        stats = self.db.pixelpets.find_one({'mint_number': mint})['orcanaut']['stats']
        for stat in stats:
            stats[stat] = min(stats[stat] + increase, 100)
        result = self.db.pixelpets.update_one({'mint_number': mint}, {'$set':{'orcanaut.stats': stats}})


