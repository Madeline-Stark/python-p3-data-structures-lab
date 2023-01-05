import ipdb
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
    # takes a list of spicy_foods 
    # and returns a list of strings with the names of each spicy food.
    return [food["name"] for food in spicy_foods]
   

def get_spiciest_foods(spicy_foods):
    # returns a list of dictionaries where the heat level of the food is greater than 5.
    return [food for food in spicy_foods if food["heat_level"] > 5]
   

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"] * "🌶"}')
    

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    # takes a list of spicy_foods and a new spicy_food and returns the original list with the new spicy_food added.

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # returns a single dictionary for the spicy food whose cuisine matches the cuisine being passed to the method.
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    heat_levels = [food["heat_level"] for food in spicy_foods] # grab all heat levels
    total = sum(heat_levels)
    return total / len(spicy_foods)
    #returns an integer representing the average heat level of all the spicy foods in the array. 
    # to derive the average of a collection, you need to calculate the total and divide number of elements in the collection.

