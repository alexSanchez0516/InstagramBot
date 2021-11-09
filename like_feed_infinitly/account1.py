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

while True:
    bot.like_timeline(amount=50)
    time.sleep(300)
