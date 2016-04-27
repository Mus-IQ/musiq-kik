import os

from kik import KikApi

BOT_USERNAME = os.environ.get('KIK_BOT_USERNAME')
BOT_API_KEY = os.environ.get('KIK_API_KEY')
token_response_json = None

bot_config = {
    "username": BOT_USERNAME,
    "key": BOT_API_KEY
}

kik = KikApi(bot_config["username"], bot_config["key"])
