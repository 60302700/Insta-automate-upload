from instagrapi import Client
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

def get_days(bot,id):
    media = bot.user_medias(id,1)
    vid = media[0].dict()['caption_text']
    days = vid[vid.find('Day '):vid.find('#meme')].rsplit()[1]
    return int(days)+1
    
def video_upload(PATH, CAPTION,bot,user,password):
    time.sleep(5)
    print(f"Logging in as {user+' '}")
    bot.login(user,password,verififcation_code=326911)
    bot.video_upload(PATH, CAPTION)
    print(f"Video uploaded: {PATH}")

def timed_login(USERNAME, PASSWORD, SESSION):
    bot = Client()
    bot.delay_range = [1, 10]  # Set delay range between 1 and 10 seconds
    bot.set_settings(SESSION)
    bot.login(USERNAME, PASSWORD)
    return bot

def scheduled_upload(ID, USERNAME, PASSWORD, SESSION):
    time.sleep(10)
    Insta = timed_login(USERNAME, PASSWORD, SESSION)
    DAY = get_days(Insta,str(ID))
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

        try: 
            #if i == 1: scheduled_upload(USER_IDS.GRANDPA.value, USERNAME, PASSWORD, SESSION)
            #if i == 2: scheduled_upload(USER_IDS.BENSON.value, USERNAME, PASSWORD, SESSION)
            #if i == 3: scheduled_upload(USER_IDS.LYING.value,USERNAME, PASSWORD, SESSION)
            #if i == 4: scheduled_upload(USER_IDS.BRO.value, USERNAME, PASSWORD, SESSION)
        except Exception as e:
            print(f"Doesn't work for {USERNAME}")
            print(e)
            continue
        # TODO: ACCOUNT 3 USER, PASS, SESSIOn
        # elif i == 4, i == 5, ... for future accounts
