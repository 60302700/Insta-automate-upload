from instagrapi import Client
import os
import time
import json

def get_session_dict_from_env(env_var):
    session_str = os.getenv(env_var)
    if session_str:
        try:
            return json.loads(session_str)  # Convert the JSON string to a dictionary
        except json.JSONDecodeError as e:
            print(f"Error decoding session data: {e}")
    return {}

def get_days(bot):
    bot.user_clips(bot.user_id,1)
    media = bot.user_clips(bot.user_id,1)
    latest = media[0]
    dict_media = latest.dict()
    cap = dict_media['caption_text']
    day = [d for d in cap[:15] if d.isdigit()]
    return int(''.join(day))+1

def video_upload(PATH, CAPTION,SESSION,bot):
    time.sleep(5)
    print(f"Logging in as {bot.user_id}")
    bot.clip_upload(PATH, CAPTION)
    print(f"Video uploaded: {PATH}")

def scheduled_upload():
    time.sleep(10)
    USERNAME = str(os.getenv('USERNAME1'))
    PASSWORD = str(os.getenv('PASSWORD1'))
    SESSION = get_session_dict_from_env(os.getenv('SESSION1'))
    Insta = Client()
    Insta.set_settings(SESSION)
    Insta.login(USERNAME, PASSWORD)
    DAY = get_days(Insta)
    PATH = "grandpa.mp4"
    CAPTION = f'''DAY {DAY} \n #meme #trending #trending #viral #instagram #explorepage #explore #instagood #love #reels #follow #trend #like #photography #india #fyp #instadaily #tiktok #foryou #trendingreels #trendingnow #style #memes #photooftheday #music #reelsinstagram #viralpost #model #insta'''
    video_upload(PATH, CAPTION,SESSION,Insta)

def scheduled_upload_benson():
    time.sleep(10)
    USERNAME = str(os.getenv('USERNAME2'))
    PASSWORD = str(os.getenv('PASSWORD2'))
    SESSION = get_session_dict_from_env(os.getenv('SESSION2'))
    Insta = Client()
    Insta.set_settings(SESSION)
    Insta.login(USERNAME, PASSWORD)
    DAY = get_days(Insta)
    PATH = "video.mp4"
    CAPTION = f"DAY {DAY} \n #meme #trending #trending #viral #instagram #explorepage #explore #instagood #love #reels #follow #trend #like #photography #india #fyp #instadaily #tiktok #foryou #trendingreels #trendingnow #style #memes #photooftheday #music #reelsinstagram #viralpost #model #insta"
    video_upload(PATH, CAPTION,SESSION,Insta)
scheduled_upload()
scheduled_upload_benson()
