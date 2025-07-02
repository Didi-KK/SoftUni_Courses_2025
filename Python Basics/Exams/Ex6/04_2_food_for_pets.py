days = int(input())
total_pet_food = float(input())


biscuits_eaten = 0
total_food_eaten = 0
total_dog_food = 0
total_cat_food = 0

for day in range(1, days +1):
    dog_food_eaten = int(input())
    cat_food_eaten = int(input())
    pet_food_per_day = dog_food_eaten + cat_food_eaten
    total_food_eaten += pet_food_per_day
    total_dog_food += dog_food_eaten
    total_cat_food += cat_food_eaten
    
    if day % 3 == 0:
        biscuits_eaten += pet_food_per_day * 0.10
        
total_pet_food_percentage = total_food_eaten / total_pet_food * 100
total_dog_food_percentage = total_dog_food / total_food_eaten * 100
total_cat_food_percentage = total_cat_food / total_food_eaten * 100


print(f"Total eaten biscuits: {round(biscuits_eaten)}gr.")
print(f"{total_pet_food_percentage:.2f}% of the food has been eaten.")
print(f"{total_dog_food_percentage:.2f}% eaten from the dog.")
print(f"{total_cat_food_percentage:.2f}% eaten from the cat.")
