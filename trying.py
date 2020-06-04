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
        print(list_of_all)



def View_ings():
    print("\n" "List of the recipes:" "\n")
    for r in catalog:
        name = r.name
        difficultylevel = r.dificulty_level
        print("Recipe name:", name + ",", "\t", "Difficulty level:", difficultylevel)

    name_of_r = input("\n" "Enter name of the recipe: ").lower()
    in_recipes = False
    for r in catalog:
        if r.name == name_of_r:
            print("\n" "The required ingredients: " "\n")
            for i in r.ingredients:
                name = i.name
                value = i.value

                print("Ingredient:", name + ",", "Value:", value)
                in_recipes = True
    if not in_recipes:
        "This recipe is not in catalog. Try again!"







