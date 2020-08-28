import requests
import telebot
import random
import pickle
import json

from telebot import types

TOKEN = "805189335:AAHJYlxi3EOSHCFQSKnKgxbNuJq3664x8kA"
#MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'
STICKER_ID = 'CAACAgIAAxkBAAMxXkMJvFktD4fRWKkTuNgG-iPxf-QAAkwAAwYumBfCY1-ip8AmlBgE'

bot = telebot.TeleBot(TOKEN)

USERS = set()

@bot.message_handler(commands=['start', 'help'])
def command_handler(message):
    bot.reply_to(message, "Fuck off")


@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo(message):
    repl = str(random.random())
    if message.from_user.id in USERS:
        repl += f"  {message.from_user.first_name}, hello, here we go again"
    bot.reply_to(message, repl)
    user = {"id" : message.from_user.id, "first_name" : message.from_user.first_name, "last_name" : message.from_user.last_name, "username" : message.from_user.username }
    #print(message.from_user)
    #USERS.add(message.from_user.id)


    fs = open('f.json', 'r').read()
    ss = "id: " + str(user["id"])
    if str(user["id"]) not in fs:
        bot.send_message(chat_id=message.chat.id,  text="Hallo there new!")

        if fs is not "":
            data = json.loads(fs)
        data[str(message.from_user.id)].append(user)
        with open('f.json', 'w') as f:
            # if user not in f:
            json.dump(data, f)
        #res = json.loads()



    open('f.json', 'r').read()
    #bot.reply_to(message, str(random.random()))



@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):

    bot.send_sticker(message.chat.id, STICKER_ID)

@bot.inline_handler(lambda query: query.query == 'text')
def query_text(inline_query):
    try:
        r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
        r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
        bot.answer_inline_query(inline_query.id, [r, r2])
    except Exception as e:
        print(e)

bot.polling(timeout=60) # инет

