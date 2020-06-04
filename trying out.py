class Ingredient:
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
            danger = line[2]
            list_of_all.append(Ingredient(name, description, danger))
    return list_of_all
database_info()


def show_description():
    bot.send_message(message.chat.id, 'Enter the name of an ingredient')

    @bot.message_handler(content_types=['text'])  # not sure

    messageis = False
    for i in list_of_all:
        if i.name == message.text:
            messageis = True
            bot.send_message(message.chat.id,"Name: ", i.name, "description: ", i.description)  # make them work for bot
        elif messageis == False:
            bot.send_message(message.chat.id, "Sorry! We do not have this ingredient in the database yet.")  # make work for bot




def read_message():
        ing = message.text.strip().split(",")
        message_list = ing
        return message_list


#check whether all ings are in the list.(done) if not report and send to main menu(done) all in "View_ingredients" function


def View_ingredients():
    list_of_absent = []
    list_of_bad = []
    ticks = 0
    for i in message_list:
        for r in list_of_all:
            if message_list(i) == r.name:
                if r.danger == "X":
                    list_of_bad.append(r.name)
                ticks+=1
            else:
                list_of_absent.append(message_list(i))
    if len(list_of_bad) > 0 and len(list_of_absent) > 0:
        bot.send_message(message.chat.id,"The dangerous ingredients are", list_of_bad)
        bot.send_message(message.chat.id,"These elements"+list_of_absent+"are not found in out database")
    elif len(list_of_bad) > 0 and len(list_of_absent) == 0:
        bot.send_message(message.chat.id,"The dangerous ingredients are", list_of_bad)
    elif len(list_of_bad) == 0 and len(list_of_absent) > 0:
        bot.send_message(message.chat.id,"There are no unhealthy ingredients found in the given list")
        bot.send_message(message.chat.id,"However, these elements"+list_of_absent+"are not found in out database")
    elif len(list_of_bad) == 0 and len(list_of_absent) > 0:
        bot.send_message(message.chat.id,"There are no unhealthy ingredients found in the given list")
    #put a function to start again

