API_TOKEN = '1088294101:AAEGUbRuAEoxSfT1NrHYxzRghlqu5zVfPiU'


class Ingredient:
    def __init__(self, name, description, danger):
        self.name = name
        self.description = description
        self.danger = danger


def database_info():
    list_of_all = []
    with open('database.txt', 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
        for line in lines:
            line = line.split(';')
            name = line[0]
            description = line[1]
            danger = line[2]
            list_of_all.append(Ingredient(name, description, danger))
    return list_of_all


def View_ingredients1(message_list, list_of_all, bot, where_send):
    message_list = message_list.replace(', ', ';')
    list_of_absent = []
    list_of_bad = []
    ing = message_list.strip().split(";")
    result = []
    for i in ing:
        result.append(i.title())
    for i in result:
        check = False
        for r in list_of_all:
            if i == r.name:
                check = True
                if r.danger == '-':
                    list_of_bad.append(i)
        if not check:
            list_of_absent.append(i)
    if len(list_of_bad) > 0 and len(list_of_absent) > 0:
        bot.send_message(where_send, "Oops! These ingredients may be dangerous for you:" + '\n'.join(list_of_bad))
        bot.send_message(where_send, "Sorry! These elements are not found in our database:" + '\n'.join(list_of_absent))
    elif len(list_of_bad) > 0 and len(list_of_absent) == 0:
        bot.send_message(where_send, "Oops! These ingredients may be dangerous for you:" + '\n'.join(list_of_bad))
    elif len(list_of_bad) == 0 and len(list_of_absent) > 0:
        bot.send_message(where_send, "Everything is safe!")
        bot.send_message(where_send, "Sorry! These elements are not found in our database:" + '\n'.join(list_of_absent))
    elif len(list_of_bad) == 0 and len(list_of_absent) > 0:
        bot.send_message(where_send, "Everything is safe!")



def View_ingredients(message_list, list_of_all, bot, where_send):
    list_of_absent = []
    list_of_bad = []
    for i in message_list:
        for r in list_of_all:
            if i == r.name:
                if r.danger == "-":
                    list_of_bad.append(r.name)
            if i != r.name:
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


def show_description(sms, to_whom, which_bot, all_list):
    tips = 0
    for i in all_list:
        if sms == i.name:
            which_bot.send_message(to_whom, i.name + '\n' + i.description)
            tips += 1
    if tips == 0:
        which_bot.send_message(to_whom, "Sorry! We do not have this ingredient in the database yet.")
