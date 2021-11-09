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

numberOfHashtags = 0

for i in data[filename]['follow_users_by_hashtags']['hashtags']:
    numberOfHashtags += 1

numberOfFollows = numberOfHashtags * 80
delay = int((8600 / numberOfFollows))

for hashtag in data[filename]['follow_users_by_hashtags']['hashtags']:
    users = bot.get_hashtag_users(hashtag=hashtag)
    for user in tqdm(users, desc='Following ' + str(len(users)) + ' users'):
        bot.follow(user_id=user)
        bot.logger.info("Waiting " + str(delay) + " seconds to not get banned")
        time.sleep(delay)
bot.logout()
