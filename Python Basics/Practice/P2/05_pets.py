from math import floor, ceil

days_away = int(input())
pet_food_available_kg = int(input())
dog_food_kg_per_day = float(input())
cat_food_kg_per_day = float(input())
tortoise_food_gr_per_day = float(input())

dog_food_consumption = float(days_away * dog_food_kg_per_day)
cat_food_consumption = float(days_away * cat_food_kg_per_day)
tortoise_food_consumption = float(days_away * tortoise_food_gr_per_day / 1000)
total_food_consumed = float(dog_food_consumption + cat_food_consumption + tortoise_food_consumption)

if pet_food_available_kg >= total_food_consumed:

    pet_food_difference = pet_food_available_kg - total_food_consumed
    pet_food_difference = floor(pet_food_difference)
    reply = f"{pet_food_difference} kilos of food left"
    print(reply)

else:
    pet_food_difference = total_food_consumed - pet_food_available_kg
    pet_food_difference = ceil(pet_food_difference)
    reply = f"{pet_food_difference} more kilos of food are needed"
    print(reply)