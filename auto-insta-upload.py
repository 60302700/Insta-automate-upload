from instagrapi import Client , delay
import os
import time
import json
import requests
from id_user import USER_IDS
from bs4 import BeautifulSoup

def get_session_dict_from_env(env_var):
    session_str = os.getenv(env_var)
    if session_str:
        try:
            return json.loads(session_str)  # Convert the JSON string to a dictionary
        except json.JSONDecodeError as e:
            print(f"Error decoding session data: {e}")
    return {}
'''def get_days(user):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    h = requests.get(f'https://www.instagram.com/{user}',headers=headers)
    print(requests.status_code)
    print(requests.text)
    soup = BeautifulSoup(h.text,'html.parser')
    posts = soup.find('meta',property="og:description")
    posts = posts.prettify()
    posts = posts[1:posts.find('Posts')]
    return int((posts.split()[-1]))'''

def get_days(bot,id):
    bot.delay[1,10]
    media = bot.user_medias(id,1)
    vid = media[0].dict()['caption_text']
    days = int(vid[vid.find(' '):vid.find('#meme')])
    return days+1
    
def video_upload(PATH, CAPTION,bot,user,password):
    time.sleep(5)
    print(f"Logging in as {user}")
    bot.login(user,password)
    bot.delay[1,10]
    bot.video_upload(PATH, CAPTION)
    print(f"Video uploaded: {PATH}")

def timed_login(USERNAME, PASSWORD, SESSION):
    bot = Client()
    bot.delay[1,10]
    bot.set_settings(SESSION)
    bot.delay[1,10]
    bot.login(USERNAME, PASSWORD)
    bot.delay[1,10]
    return bot

def scheduled_upload(ID, USERNAME, PASSWORD, SESSION):
    time.sleep(10)
    Insta = timed_login(USERNAME, PASSWORD, SESSION)
    DAY = get_days(Insta,ID)
    PATH = f"{USERNAME.replace('.','_')}.mp4"
    CAPTION = f'''Day {DAY} #meme #trending #trending #viral #instagram #explorepage #explore #instagood #love #reels #follow #trend #like #photography #india #fyp #instadaily #tiktok #foryou #trendingreels #trendingnow #style #memes #photooftheday #music #reelsinstagram #viralpost #model #insta'''
    if ID == USER_IDS.LYING.value: CAPTION += '#whyualwayslying #why'
    video_upload(PATH, CAPTION,Insta,USERNAME,PASSWORD)


if __name__ == "__main__":
    NO_OF_ACCOUNTS = len(USER_IDS)

    for i in range(1,NO_OF_ACCOUNTS+1):
        USERNAME=str(os.getenv(f'USERNAME{i}'))
        PASSWORD=str(os.getenv(f'PASSWORD{i}'))
        SESSION=get_session_dict_from_env(os.getenv(f'SESSION{i}'))

        if i == 1: scheduled_upload(USER_IDS.GRANDPA.value, USERNAME, PASSWORD, SESSION)
        elif i == 2: scheduled_upload_benson(USER_IDS.BENSON.value, USERNAME, PASSWORD, SESSION)
        elif i == 3: scheduled_upload_sc(USER_IDS.LYING.value,USERNAME, PASSWORD, SESSION)
        elif i == 4: scheduled_upload_aq(USER_IDS.BRO.value, USERNAME, PASSWORD, SESSION)
        # TODO: ACCOUNT 3 USER, PASS, SESSIOn
        # elif i == 4, i == 5, ... for future accounts
