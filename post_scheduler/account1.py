import sys
import os
import glob
import json
import time
from io import open
from tqdm import tqdm
sys.path.append('..')
from instagram_bot import Bot

with open('../config.json') as f:
    data = json.load(f)

base = os.path.basename(__file__)
filename = os.path.splitext(base)[0]

posted_pic_list = []
try:
    with open('pics.txt', 'r', encoding='utf8') as f:
        posted_pic_list = f.read().splitlines()
except Exception:
    posted_pic_list = []

postsPerDay = data[filename]['post_scheduler']['postsPerDay']
timeout = int((84600 / postsPerDay))

bot = Bot()
bot.login(username=data[filename]['username'], password=data[filename]['password'])

while True:
    pics = glob.glob("./pics/*.jpg")
    pics = sorted(pics)
    try:
        for pic in pics:
            if pic in posted_pic_list:
                continue

            caption = pic[:-4].split(" ")
            caption = " ".join(caption[1:])

            print("upload: " + caption)
            bot.upload_photo(pic, caption=caption)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
                # snd msg
                break

            if pic not in posted_pic_list:
                posted_pic_list.append(pic)
                with open('pics.txt', 'a', encoding='utf8') as f:
                    f.write(pic + "\n")

            for i in tqdm(range(0, timeout), desc="Waiting " + str(timeout) + " seconds"):
                time.sleep(1)


    except Exception as e:
        print(str(e))
    time.sleep(60)
