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
    bot.send_message(message.chat.id, "Please enter the ingredients with comma(,) after each")




















@bot.message_handler(content_types=['text'])
def send_text(message):#red marks from here
    if message.text in data:
        bot.send_message(message.chat.id, 'Yeah, we have this in the list')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Прощай, создатель') #to here

class Ingredient: #test from here
    def __init__(self, name, description):
        self.name = name
        self.description = description



list_of_all = []

def database_info():
    with open('database.txt') as f:
        for line in f:
            line = line.strip().split(';')
            name = line[0]
            description = line[1]
            list_of_all.append(Ingredient(name, description))
    return list_of_all



def display_ings(message, ):
    if message.text in data:
        bot.send_message(message.chat.id, 'Yeah, we have this in the list')#to here

bot.polling()
