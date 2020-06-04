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
            list_of_all.append(Ingredient(name, description))
    return list_of_all


def checking_if_inlist(message_list):
    for i in message_list:



def read_message(message):
        ing = message.strip().split(",")
        message_list = ing
        return message_list





def writing response
