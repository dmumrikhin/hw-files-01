from pprint import pprint

with open('recipes.txt') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        ingredient = []
        for _ in range(ingredients_count):
            emp = file.readline().strip()
            ingredient_name, quantity, measure = emp.split(' | ')
            ingredient.append(
                {'ingredient_name': ingredient_name,
                 'quantity': quantity,
                 'measure': measure}
            )
        cook_book[dish_name] = ingredient
        file.readline()

pprint(cook_book) #, sort_dicts=False)