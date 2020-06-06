import telebot
import config
from config import database_info
from config import View_ingredients
from config import show_description1

bot = telebot.TeleBot(config.API_TOKEN)
list_of_all = database_info()


@bot.message_handler(commands=['start'])  # command to start the bot
def start_message(message):
    bot.send_message(message.chat.id, "Hi, let's be healthy and safe together!""\n"  # Answer to the message
                                      "If you want to check whether your products contain bad ingredients, enter /1""\n"  # checking for bad
                                      "If you want to know more about an ingredient enter /2""\n"
                                      "If you want to say goodbye than enter'Bye'")  # 2 output description


@bot.message_handler(commands=['1'])
def option_one(message):
    bot.send_message(message.chat.id, 'Enter the ingredients with comma(,) after each')

    @bot.message_handler(content_types=['text'])
    def reading_the_answer(message):
        ing = message.text.strip().split(",")
        message_list = ing
        View_ingredients(message_list, list_of_all, bot, message.chat.id)


@bot.message_handler(commands=['2'])
def know_more(message):
    bot.send_message(message.chat.id, 'Enter the name of an ingredient')

    @bot.message_handler(content_types=['text'])
    def finding_description(message):
        text = message.text
        text = text.title()
        to_where = message.chat.id
        bot.send_message(message.chat.id, show_description1(text, to_where, bot, list_of_all))


bot.polling()
