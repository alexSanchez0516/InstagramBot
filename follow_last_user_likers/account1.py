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

numberOfFollows = data[filename]['follow_last_user_likers']['numberOfFollows']
delay = int((84600 / numberOfFollows))

medias = bot.get_user_medias(user_id=data[filename]['follow_last_user_likers']['username'], filtration=False)

if medias:
    likers = bot.get_media_likers(medias[0])
    for liker in tqdm(range(0, data[filename]['follow_last_user_likers']['numberOfFollows']), desc='Following ' + str(data[filename]['follow_last_user_likers']['numberOfFollows']) + ' users'):
        bot.follow(liker)
        bot.logger.info("Waiting " + str(delay) + " seconds to not get banned")
        time.sleep(delay)
bot.logout()
