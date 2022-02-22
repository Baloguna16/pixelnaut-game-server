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
    if last_fed_duration > FEEDING_TIMEOUT:
        db.reset_stats(mint)
    elif last_fed_duration > FEEDING_TIMEOUT/2:
        stat_increase = ceil(0.055*(last_fed_duration - FEEDING_TIMEOUT/2)**2)
        result = db.increase_stats(mint, stat_increase)
    db.feed_fish(mint)
def clean_tank(mint):
    _, last_cleaned_duration = get_durations(mint)

def get_durations(mint):
    result = db.get_state(mint)
    now = datetime.timestamp(datetime.now())
    last_fed_duration = now - result['orcanaut']['last_fed']
    last_cleaned_duration = now - result['tank']['last_cleaned']
    return (last_fed_duration, last_cleaned_duration)