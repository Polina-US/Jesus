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


everything_list = database_info()
message_list = 'Alcohol, algin, leaf oil, Benzyl Salicylate, oehgorhworhgiu '
message_list = message_list.replace(', ', ';')
list_of_absent = []
list_of_bad = []
ing = message_list.strip().split(";")
result = []
for i in ing:
    result.append(i.title())
for i in result:
    check = False
    for r in everything_list:
        if i == r.name:
            check = True
            if r.danger == '-':
                list_of_bad.append(i)
    if check == False:
        list_of_absent.append(i)


print(list_of_absent)
if len(list_of_bad) > 0 and len(list_of_absent) > 0:
    print("Oops! These ingredients may be dangerous for you:\n " + '\n'.join(list_of_bad))
    print("Sorry! These elements are not found in our database:\n" + '\n'.join(list_of_absent))
elif len(list_of_bad) > 0 and len(list_of_absent) == 0:
    print("Oops! These ingredients may be dangerous for you:\n" + '\n'.join(list_of_bad))
elif len(list_of_bad) == 0 and len(list_of_absent) > 0:
    print("Everything is safe!")
    print("Sorry! These elements are not found in our database:\n" + '\n'.join(list_of_absent))
elif len(list_of_bad) == 0 and len(list_of_absent) > 0:
    print("Everything is safe!")




