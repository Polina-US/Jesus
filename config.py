API_TOKEN = '1088294101:AAEGUbRuAEoxSfT1NrHYxzRghlqu5zVfPiU'


class Ingredient:
    def __init__(self, name, description, danger):
        self.name = name
        self.description = description
        self.danger = danger


def database_info():
    with open('database.txt') as f:
        list_of_all = []
        for line in f:
            line = line.strip().split(';')
            name = line[0]
            description = line[1]
            danger = line[2]
            list_of_all.append(Ingredient(name, description, danger))
    return list_of_all


def read_message():
        ing = message.text.strip().split(",")
        message_list = ing
        return message_list


def View_ingredients(message_ans, classes_list, bot, where_send):
    list_of_absent = []
    list_of_bad = []
    for i in message_ans:
        for r in classes_list:
            if i == r.name:
                if r.danger == "-":
                    list_of_bad.append(r.name)
            else:
                list_of_absent.append(i)
    if len(list_of_bad) > 0 and len(list_of_absent) > 0:
        bot.send_message(where_send, "Oops! These ingredients may be dangerous for you:", list_of_bad)
        bot.send_message(where_send, "Sorry! These elements are not found in our database:", list_of_absent)
    elif len(list_of_bad) > 0 and len(list_of_absent) == 0:
        bot.send_message(where_send, "Oops! These ingredients may be dangerous for you:", list_of_bad)
    elif len(list_of_bad) == 0 and len(list_of_absent) > 0:
        bot.send_message(where_send, "Everything is safe!")
        bot.send_message(where_send, "Sorry! These elements are not found in our database:", list_of_absent)
    elif len(list_of_bad) == 0 and len(list_of_absent) > 0:
        bot.send_message(where_send, "Everything is safe!")


def show_description():
    messageis = False
    for i in list_of_all:
        if i.name == message.text:
            messageis = True
            bot.send_message(message.chat.id,"Name: ", i.name, "description: ", i.description)  # make them work for bot
        elif messageis == False:
            bot.send_message(message.chat.id, "Sorry! We do not have this ingredient in the database yet.")  # make work for bot


