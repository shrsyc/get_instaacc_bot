import time
import telebot
import os

API_KEY=os.environ['API_KEY_GETINSTAACC']
bot = telebot.TeleBot(API_KEY)

def findat(msg):
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start']) 
def send_welcome(message):
    bot.reply_to(message, ':) hallo enter the  instagram username')
    


@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': 
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)
        bot.reply_to(message,"enter the next username")

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep()

