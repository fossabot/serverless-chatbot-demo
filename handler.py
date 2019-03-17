import json
import logging
import os
import random
import time

from emoji import emojize
from telegram import Bot, Update

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

RESPONSE = {
    "OK": {
        'statusCode': 200,
        'headers': {'Content-type': 'application/json'},
        'body': json.dumps("Ok")
    },
    "ERROR": {
        'statusCode': 400,
        'body': json.dumps("Something went wrong")
    }
}


def configure_telegram():
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
    if not TELEGRAM_TOKEN:
        logging.error(
            'TELEGRAM_TOKEN Not found, it must be set before moving forward.')
        raise NotImplementedError
    return Bot(TELEGRAM_TOKEN)


def populate_excuse():
    global excuseDict
    excuseDict = {}
    officeExcuse = (
        "I missed the office because ozone fluttered my car tire in the air.", "The pressure cooker in my house exploded and scared the maid so I had to stay at home", "I was blocked by the tax department of the housing committee who raided my house.", "Loki Chan was again in my lunch box, and I was very upset to go on time")
    birthdayExcuse = (
        "I remember if I did not eat canteen for lunch!",
        "The weather has made me do this. Seriously. In May, to cry loudly in Mumbai! Are not you born in October?", "what!!! I was doing a favor to you by mistake, and was trying to teach you the art of forgiveness.", "I was kidnapped by the aliens and they wiped me from my memory one day ... So, I will remember tomorrow.")
    anniversaryExcuse = (
        "I thought our wedding anniversary was the day we met, on that day we did not make it official.", "I wanted to surprise you - would not you be surprised if I really remembered it, right? Understandable", "I.P.L. Tickets were sold, so I decided that we can celebrate next week.", "I remembered, but I forgot on the way I passed through the Saki Naka, remember?")
    excuseDict['missed office'] = officeExcuse
    excuseDict['forgot birthday'] = birthdayExcuse
    excuseDict['forgot anniversary'] = anniversaryExcuse


def webhook(event, context):
    bot = configure_telegram()
    logging.info('Event: {}'.format(event))
    populate_excuse()
    if event.get('httpMethod') == 'POST' and event.get('body'):
        logging.info("Message successfully received")
        update = Update.de_json(json.loads(event.get('body')), bot)
        chat_id = update.message.chat_id
        text = update.message.text
        if text == '/start':
            text = """Hello, human! I am an excuse bot, built with Python and the Serverless Framework. I help with excuses {}.\n\
You can take a look at my source code here: https://github.com/vaibhavsingh97/serverless-chatbot-demo.\n\
Found a {}, please drop a tweet to my creator: https://twitter.com/vaibhavsingh97. Happy botting!""".format(emojize("! :laughing:", use_aliases=True), emojize("! :bug:", use_aliases=True))
            bot.send_chat_action(chat_id=chat_id, action="TYPING")
            time.sleep(2)
            bot.send_message(chat_id=chat_id, text=text)
        elif "missed" in text and "office" in text:
            headers = {
                "Accept": "application/json",
                "User-Agent": "excuse bot (https://github.com/vaibhavsingh97/serverless-chatbot-demo)"
            }
            arr = excuseDict['missed office']
            text = arr[random.randint(0, len(arr))]
            bot.send_chat_action(chat_id=chat_id, action="TYPING")
            time.sleep(2)
            bot.send_message(chat_id=chat_id, text=text)
        elif "forgot" in text and "birthday" in text:
            headers = {
                "Accept": "application/json",
                "User-Agent": "excuse bot (https://github.com/vaibhavsingh97/serverless-chatbot-demo)"
            }
            arr = excuseDict['forgot birthday']
            text = arr[random.randint(0, len(arr))]
            bot.send_chat_action(chat_id=chat_id, action="TYPING")
            time.sleep(2)
            bot.send_message(chat_id=chat_id, text=text)
        elif "forgot" in text and "anniversary" in text:
            headers = {
                "Accept": "application/json",
                "User-Agent": "excuse bot (https://github.com/vaibhavsingh97/serverless-chatbot-demo)"
            }
            arr = excuseDict['forgot anniversary']
            text = arr[random.randint(0, len(arr))]
            bot.send_chat_action(chat_id=chat_id, action="TYPING")
            time.sleep(2)
            bot.send_message(chat_id=chat_id, text=text)
        elif text == '/help':
            text = """
Hello! Excuse bot welcomes you on the telegram!
Here's the commands:
- /start - to get know more about Excuse Bot
- /help - to view help text
This bot is being worked on, so it may break sometimes. Contact @vaibhavsingh97 on twitter \
or open issue [here](https://github.com/vaibhavsingh97/serverless-chatbot-demo).
"""
            bot.send_chat_action(chat_id=chat_id, action="TYPING")
            time.sleep(2)
            bot.send_message(chat_id=chat_id, text=text, parse_mode="MARKDOWN")
        logging.info("Message successfully sent")
        # RESPONSE["OK"]["body"] = json.dumps("Message Sent")
        return RESPONSE["OK"]
    return RESPONSE["ERROR"]


def set_webhook(event, context):
    logging.info('Event: {}'.format(event))
    bot = configure_telegram()
    url = 'https://{}/{}'.format(
        event.get('headers').get('Host'),
        event.get('requestContext').get('stage')
    )
    webhook = bot.set_webhook(url)

    if webhook:
        RESPONSE["OK"]["body"] = json.dumps("Webhook URL successfully set.")
        return RESPONSE["OK"]

    return RESPONSE["ERROR"]


def get_webhook_info(event, context):
    logging.info('Event: {}'.format(event))
    bot = configure_telegram()
    webhook_info = bot.get_webhook_info()
    logging.info('Event: {}'.format(webhook_info))
    if webhook_info:
        RESPONSE["OK"]["body"] = str(webhook_info)
        return RESPONSE["OK"]
    return RESPONSE["ERROR"]
