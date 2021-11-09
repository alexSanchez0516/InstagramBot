import sys
import os
import json
import random
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

for i in data[filename]['comment_hashtags']['hashtags']:
    numberOfHashtags += 1

commentsInTotal = (numberOfHashtags * data[filename]['comment_hashtags']['numberOfCommentsPerHashtag'])
delay = int((4600 / commentsInTotal))

for hashtag in data[filename]['comment_hashtags']['hashtags']:
    commented = 0
    failedToComment = 0

    bot.logger.info("Getting medias for " + hashtag)
    medias = bot.get_total_hashtag_medias(hashtag=hashtag, amount=data[filename]['comment_hashtags']['numberOfCommentsPerHashtag'])
    for media in tqdm(medias, desc="Commeting on " + str(len(medias)) + " medias"):
        time.sleep(2)
        bot.logger.info("Commenting on media " + str(media))
        try:
            bot.comment(media_id=media, comment_text=random.choice(data[filename]['comment_hashtags']['commentText']))
            bot.logger.info("Waiting " + str(delay) + " seconds to not get banned")
            time.sleep(delay)
            commented += 1
        except Exception as e:
            bot.logger.error("Error commenting on media\n" + str(e))
            failedToComment += 1

    bot.logger.info("You commented " + str(commented) + " medias")
    bot.logger.info("You failed to comment " + str(failedToComment) + " medias")
bot.logout()
