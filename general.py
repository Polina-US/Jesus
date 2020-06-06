import telebot
import config
from config import database_info
from config import View_ingredients
from config import read_message
from config import show_description

bot = telebot.TeleBot(config.API_TOKEN)
list_of_all = database_info()



@bot.message_handler(commands=['start'])  # command to begin, try to switch line 12 with line 13 to make the fuction work while put in any place
def start_message(message):
    bot.send_message(message.chat.id, "Hi, let's be healthy and safe together!""\n"  # Answer to the message
                                      "If you want to check whether your products contain bad ingredients, enter /1""\n"  # 1 option to see whether a list of ingredients contain a "bad" ones (the ingredients with comma(,) after each)
                                      "If you want to know more about an ingredient enter /2""\n"
                                      "If you want to say goodbye than enter'Bye'")  # 2 option to see its description name

@bot.message_handler(commands=['1'])
def option_one(message):
    bot.send_message(message.chat.id, 'Enter the ingredients with comma(,) after each')
    @bot.message_handler(content_types=['text'])
    def reading_the_answer(message):
        ing = message.text.strip().split(",")
        message_list = ing
        View_ingredients(message_list, list_of_all, bot, message.chat.id )




@bot.message_handler(commands=['2'])
def know_more(message):
    bot.send_message(message.chat.id, 'Enter the name of an ingredient')
    show_description()

@bot.message_handler(content_types=['text'])
def some_issues(message):
    bot.send_message(message.chat.id, 'You have entered the message I cannot understand. try again!')


# def send_text(message):
#     to_whom = message.chat.id
#     if message.text == '1':  # code for option 1
#         bot.send_message(message.chat.id, 'Enter the ingredients with comma(,) after each')
#         @bot.message_handler(content_types=['text'])
#         d
#         ing = message.text.strip().split(",")
#         message_list = ing
#         View_ingredients(message_list, list_of_all, bot, to_whom)
#     elif message.text == '2':
#         bot.send_message(message.chat.id, 'Enter the name of an ingredient')
#         show_description()
#     elif message.text == 'Bye'.lower():
#         bot.send_message(message.chat.id, 'Goodbye!')
#     else:
#         bot.send_message(message.chat.id, 'You have entered the message I cannot understand. try again!')



bot.polling()

