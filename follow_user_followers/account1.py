import sys
import os
import json
import time
from tqdm import tqdm
sys.path.append('..')
from instagram_bot import Bot

with open('../config.json') as f:
    data = json.load(f)

base = os.path.basename(__file__)
filename = os.path.splitext(base)[0]

bot = Bot()
bot.login(username=data[filename]['username'], password=data[filename]['password'])

numberOfFollows = data[filename]['follow_user_followers']['numberOfFollows']
delay = int((1600 / numberOfFollows))

followers = bot.get_user_followers(user_id=data[filename]['follow_user_followers']['user'], nfollows=data[filename]['follow_user_followers']['numberOfFollows'])

for follower in followers:
    followerUsername = bot.get_username_from_user_id(user_id=follower)
    bot.follow(user_id=follower)
    bot.logger.info("Waiting " + str(delay) + " seconds to not get banned")
    time.sleep(delay)
bot.logout()
