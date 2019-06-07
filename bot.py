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

#result = requests.get("https://api.telegram.org/bot676277323:AAHEy8kKAbvNZj3KtHPQBDyat8RyBXJCmlU/getme")
#result = requests.get("https://api.telegram.org/bot676277323:AAHEy8kKAbvNZj3KtHPQBDyat8RyBXJCmlU/getUpdates")
#result = result.json()

send_message("bot testing python2", "728810316")