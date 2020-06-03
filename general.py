import telebot
import config

from telebot import apihelper
bot = telebot.TeleBot(config.API_TOKEN)
apihelper.proxy = {'https': 'socks5://54.38.195.161:45117'}
with open('database.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()


@bot.message_handler(commands=['start'])  # command to begin
def start_message(message):
    bot.send_message(message.chat.id, "Hi, let's be healthy and safe together!")  # Answer to the message


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text in data:
        bot.send_message(message.chat.id, 'Yeah, we have this in the list')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling()
