from datetime import datetime
from api.database import mongodriver
db = mongodriver.Database()
from math import ceil

FEEDING_TIMEOUT = 60
CLEANING_TIMEOUT = 60*7

def check_timeouts(mint):
    last_fed_duration, last_cleaned_duration = get_durations(mint)
    if last_fed_duration > FEEDING_TIMEOUT or last_cleaned_duration > CLEANING_TIMEOUT:
        db.reset_stats(mint)

def feed_fish(mint):
    last_fed_duration, _ = get_durations(mint)
    db.feed_fish(mint)
    if last_fed_duration > FEEDING_TIMEOUT:
        db.reset_stats(mint)
        db.set_coin_balance(mint, 0)
        return -1
    elif last_fed_duration > FEEDING_TIMEOUT/2:
        stat_increase = ceil(0.055*(last_fed_duration - FEEDING_TIMEOUT/2)**2)
        result = db.increase_stats(mint, stat_increase)
        balance = db.get_coin_balance(mint)
        db.set_coin_balance(mint, balance + stat_increase)
        return  stat_increase
    return 0
def clean_tank(mint):
    _, last_cleaned_duration = get_durations(mint)
    db.clean_tank(mint)
    if last_cleaned_duration > CLEANING_TIMEOUT:
        db.reset_stats(mint)
        db.set_coin_balance(mint, 0)
        return -1
    elif last_cleaned_duration > CLEANING_TIMEOUT/2:
        stat_increase = ceil(0.0028*(last_cleaned_duration - FEEDING_TIMEOUT/2)**2)
        result = db.increase_stats(mint, stat_increase)
        balance = db.get_coin_balance(mint)
        db.set_coin_balance(mint, balance + stat_increase)
        return stat_increase
    return 0

def get_durations(mint):
    result = db.get_state(mint)
    now = datetime.timestamp(datetime.now())
    last_fed_duration = now - result['orcanaut']['last_fed']
    last_cleaned_duration = now - result['tank']['last_cleaned']
    return (last_fed_duration, last_cleaned_duration)