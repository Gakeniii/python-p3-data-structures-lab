spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    foods = [food ["name"] for food in spicy_foods]
    return foods
print(get_names(spicy_foods))

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
print(get_spiciest_foods(spicy_foods))

def print_spicy_foods(spicy_foods):
    for each_food in spicy_foods:

        name = each_food["name"]
        cuisine = each_food["cuisine"]
        heat_level = each_food["heat_level"]*"🌶"
        
        print(f'{name} ({cuisine}) | Heat Level: {heat_level}')
        
print(print_spicy_foods(spicy_foods))


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():
            return food
    return None
print(get_spicy_food_by_cuisine(spicy_foods, "Thai"))
print(get_spicy_food_by_cuisine(spicy_foods, "American"))
print(get_spicy_food_by_cuisine(spicy_foods, "Sichuan"))


def print_spiciest_foods(spicy_foods):
    spiciest_food = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_food)
print_spiciest_foods(spicy_foods)
        

def get_average_heat_level(spicy_foods):
    total = sum(food["heat_level"] for food in spicy_foods)
    num_food = len(spicy_foods)
    average_heat_level = total // num_food
    return average_heat_level
print(get_average_heat_level(spicy_foods))
    


spicy_food = [
    {
        "name": "Nyama Choma",
        "cuisine": "Kenyan",
        "heat_level": 6,
    },
]

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
print(create_spicy_food(spicy_foods, spicy_food))

