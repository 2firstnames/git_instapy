# -*- coding: UTF-8 -*-
import time
from datetime import datetime
from pytz import timezone
tz = timezone('EST')
import schedule
import traceback
import requests

from instapy import InstaPy
from instapy import smart_run

insta_username = 'active_vie'
insta_password = 'k2c3m9'

#### START TELEGRAM ALERT CODE ####
import json 
import requests

TOKEN = "676277323:AAHEy8kKAbvNZj3KtHPQBDyat8RyBXJCmlU"
CHAT_ID = "728810316"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
#### END TELEGRAM ALERT CODE ####

def get_session():
    session = InstaPy(username=insta_username, password=insta_password, headless_browser=True, nogui=True,multi_logs=False)
    return session

def follow():
    # Send notification to my Telegram
    send_message('InstaPy Follower Started @ {}'.format(datetime.now(tz)),"728810316")

    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        counter = 0

        while counter < 5:
            counter += 1

            try:
                # settings
                session.set_relationship_bounds(enabled=True, potency_ratio=1.21)

                # activity
                session.follow_by_tags(['fitness', 'yoga'], amount=20)
                session.follow_user_followers(['gymshark', 'zyiaactive','bootybandsofficial','alphalete','squat_wolf','ryu_apparel','gymtopz_ve','koral','varley','p.e.nation','michi_ny','squats_fitness_apparel','muscleclub','vimmia_active','karma_athletics','heroinesport','brazilwear','rhoneapparel','eysommenswear','wearittoheart','sukishufu','tenthousandgear','krissycela','fitgurlmel','katiesonier','natacha.oceane','brittnebabe'], amount=10, randomize=True)
                #session.follow_by_tags(               ['fitness','healthy','gym','motivation','workout','fit','fitfam','health','eatclean','fitspo'], amount=10)
                #session.follow_by_tags(                    ['fitnessmotivation','nutrition','fitquote','girlwholift','personaltrainer'], amount=5)
                #session.unfollow_users(amount=25, allFollowing=True,                                       style="LIFO", unfollow_after=3 * 60 * 60, sleep_delay=450)

            except Exception:
                print(traceback.format_exc())

    # Send notification to my Telegram
    send_message('InstaPy Follower Stopped @ {}'.format(datetime.now(tz)) , "728810316")


def unfollow():
    send_message('InstaPy Unfollowing Started @ {}'.format(datetime.now(tz)) , "728810316")

    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        try:
            # settings
            session.set_relationship_bounds(enabled=False, potency_ratio=1.21)

            # actions
            session.unfollow_users(amount=600, allFollowing=True, style="RANDOM", sleep_delay=450)

        except Exception:
            print(traceback.format_exc())

    send_message('InstaPy Unfollower Stopped @ {}'.format(datetime.now(tz)) , "728810316")


def xunfollow():
    send_message('InstaPy Unfollower Wednesday Started @ {}'.format(datetime.now(tz)) , "728810316")

    # get a session!
    session = get_session()

    # let's go!
    with smart_run(session):
        try:
            # settings
            session.set_relationship_bounds(enabled=False, potency_ratio=1.21)

            # actions
            session.unfollow_users(amount=1000, allFollowing=True, style="RANDOM", unfollow_after=3 * 60 * 60,sleep_delay=450)

        except Exception:
            print(traceback.format_exc())

    send_message('InstaPy Follower Wednesday Stopped @ {}'.format(datetime.now(tz)) , "728810316")


# schedulers
schedule.every().day.at("09:30").do(follow)
schedule.every().day.at("13:30").do(follow)
schedule.every().day.at("17:30").do(follow)

schedule.every().day.at("00:05").do(unfollow)

schedule.every().wednesday.at("03:00").do(xunfollow)

follow()
unfollow()
xunfollow()

while True:
    schedule.run_pending()
    time.sleep(1)
