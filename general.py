import telebot
import config

from telebot import apihelper

bot = telebot.TeleBot(config.API_TOKEN)
apihelper.proxy = {'https': 'socks5://54.38.195.161:45117'}
with open('database.txt', 'r', encoding='utf-8') as f:
    data = f.read().splitlines()

database_info()

@bot.message_handler(commands=['start'])  # command to begin, try to switch line 12 with line 13 to make the fuction work while put in any place
def start_message(message):
    bot.send_message(message.chat.id, "Hi, let's be healthy and safe together!""\n" # Answer to the message
                     "If you want to check whether your products contains bad ingredients, enter 1""\n"   # 1 option to see whether a list of ingredients contain a "bad" ones (the ingredients with comma(,) after each)
                     "If you want to know more about an ingredient enter 2""\n"
                     "If you want to say goodbye than enter'Bye'")  # 2 option to see its description name


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 1:#code for option 1
        bot.send_message(message.chat.id, 'Enter the ingredients with comma(,) after each')
        @bot.message_handler(content_types=['text'])#not sure
        read_message()
        View_ingredients()
        start_message() #not sure
    elif message.text == 2:#code for option 2
        show_description()
        start_message() #not sure
    elif message.text == 'Bye'.lower():
        bot.send_message(message.chat.id, 'Goodbye, creator!')
    else:
        bot.send_message(message.chat.id, 'You have entered the message I cannot understand. try again!')
        start_message()





bot.polling()
