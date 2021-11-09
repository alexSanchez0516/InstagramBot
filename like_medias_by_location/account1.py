import json
import random
import time
import sys
import os
from tqdm import tqdm
sys.path.append('..')
from instagram_bot import Bot

with open('../config.json') as f:
    data = json.load(f)

base = os.path.basename(__file__)
filename = os.path.splitext(base)[0]

bot = Bot()
bot.login(username=data[filename]['username'], password=data[filename]['password'])

bot.like_location_feed(place=data[filename]['like_medias_by_location']['location'], amount=data[filename]['like_medias_by_location']['numberOfLikes'])

bot.logout()
