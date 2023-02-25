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
                 'quantity': int(quantity),
                 'measure': measure}
            )
        cook_book[dish_name] = ingredient
        file.readline()

# pprint(cook_book) #, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    for dish in dishes:
        for key, value in cook_book.items():
            if key == dish:
                for item in value:
                    if item['ingredient_name'] in shop_dict:
                        shop_dict[item['ingredient_name']]['quantity'] += item['quantity'
                            ] * person_count
                    else:
                        ingredient_quantity = {}
                        ingredient_quantity['measure'] = item['measure']
                        ingredient_quantity['quantity'] = item['quantity'] * person_count
                        shop_dict[item['ingredient_name']] = ingredient_quantity
    return(shop_dict) 


pprint(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))



