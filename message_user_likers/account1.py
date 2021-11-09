import json
import time
import random
import sys
import os
sys.path.append('..')
from tqdm import tqdm
from instagram_bot import Bot

with open('../config.json') as f:
    data = json.load(f)

base = os.path.basename(__file__)
filename = os.path.splitext(base)[0]

bot = Bot()
bot.login(username=data[filename]['username'], password=data[filename]['password'])

users = bot.get_user_likers(user_id=data[filename]['message_users_likers']['user'], media_count=1)

numberOfMessages = data[filename]['message_users_likers']['numberOfMessages']
delay = int((84600 / numberOfMessages))

count = 0


for user in tqdm(users, desc="Messaging " + str(numberOfMessages) + " users"):
    if count >= numberOfMessages:
        break
    try:
        bot.send_message(text=data[filename]['message_users_likers']['text'], user_ids=user)
        bot.logger.info("Message sent succesfully!")
        count += 1
        bot.logger.info("Waiting " + str(delay) + " seconds to not get banned")
        time.sleep(delay)
    except Exception as e:
        bot.logger.error(e)
bot.logout()
