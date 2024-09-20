from instagrapi import Client
import os
import time
import json
import requests
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
    media = bot.user_medias(id,1)
    latest = media[0]
    dict_media = latest.dict()
    cap = dict_media['caption_text']
    day = [d for d in cap[:15] if d.isdigit()]
    return int(''.join(day))+1



def video_upload(PATH, CAPTION,bot):
    time.sleep(5)
    print(f"Logging in as {bot.user_id}")
    bot.clip_upload(PATH, CAPTION)
    print(f"Video uploaded: {PATH}")
    bot.logout()

def scheduled_upload():
    time.sleep(10)
    USERNAME = str(os.getenv('USERNAME1'))
    PASSWORD = str(os.getenv('PASSWORD1'))
    SESSION = get_session_dict_from_env(os.getenv('SESSION1'))
    id = 67987126316
    Insta = Client()
    Insta.login(USERNAME, PASSWORD)
    Insta.set_settings(SESSION)
    DAY = get_days(Insta,id)
    PATH = "grandpa.mp4"
    CAPTION = f'''DAY {DAY} \n #meme #trending #trending #viral #instagram #explorepage #explore #instagood #love #reels #follow #trend #like #photography #india #fyp #instadaily #tiktok #foryou #trendingreels #trendingnow #style #memes #photooftheday #music #reelsinstagram #viralpost #model #insta'''
    video_upload(PATH, CAPTION,Insta)

def scheduled_upload_benson():
    time.sleep(10)
    USERNAME = str(os.getenv('USERNAME2'))
    PASSWORD = str(os.getenv('PASSWORD2'))
    SESSION = get_session_dict_from_env(os.getenv('SESSION2'))
    id = 67538479126
    Insta = Client()
    Insta.login(USERNAME, PASSWORD)
    Insta.set_settings(SESSION)
    DAY = get_days(Insta,id)
    PATH = "video.mp4"
    CAPTION = f"DAY {DAY} \n #meme #trending #trending #viral #instagram #explorepage #explore #instagood #love #reels #follow #trend #like #photography #india #fyp #instadaily #tiktok #foryou #trendingreels #trendingnow #style #memes #photooftheday #music #reelsinstagram #viralpost #model #insta"
    video_upload(PATH, CAPTION,Insta)
scheduled_upload()
#scheduled_upload_benson()
