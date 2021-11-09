import sys
import os
import time
import json
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

for i in data[filename]['like_hashtags']['hashtags']:
    numberOfHashtags += 1

numberOfLikes = (data[filename]['like_hashtags']['numberOfLikesPerHashtag'] * numberOfHashtags)
delay = int((4600 / numberOfLikes))

for hashtag in data[filename]['like_hashtags']['hashtags']:
    medias = bot.get_total_hashtag_medias(hashtag=hashtag, amount=data[filename]['like_hashtags']['numberOfLikesPerHashtag'])
    for media in medias:
        bot.like(media_id=media)
        bot.logger.info("Media " + str(media) + " liked succesfully")
        bot.logger.info("Waiting " + str(delay) + " seconds to not get banned")
        time.sleep(delay)
bot.logout()
