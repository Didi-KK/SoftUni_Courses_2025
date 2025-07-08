percentage_fat = int(input())
percentage_protein = int(input())
percentage_carbs = int(input())
total_calories = int(input())
percentage_water_content = int(input())

fat_grams = percentage_fat * total_calories / 9
protein_grams = percentage_protein * total_calories / 4
carbs_grams = percentage_carbs * total_calories / 4
all_food_grams = fat_grams + protein_grams + carbs_grams
calories_grams = total_calories / all_food_grams
calories = calories_grams * (100 - percentage_water_content)

print(f'{calories:.4f}')
