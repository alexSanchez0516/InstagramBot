import json
import os
import sys
import time
import random
sys.path.append('..')
from instagram_bot import Bot

with open('../config.json') as f:
    data = json.load(f)

base = os.path.basename(__file__)
filename = os.path.splitext(base)[0]

bot = Bot()
bot.login(username=data[filename]['username'], password=data[filename]['password'])

bot.unfollow_non_followers(n_to_unfollows=data[filename]['unfollow_non_followers']['numberOfUnfollows'])
bot.logout()
