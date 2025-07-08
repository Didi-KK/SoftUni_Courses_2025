from math import ceil, floor

days_away = int(input())

food_left = int(input())

deer_one_food = float(input())
deer_two_food = float(input())
deer_three_food = float(input())

food_eaten = days_away * (deer_one_food + deer_two_food + deer_three_food)

diff = abs(food_left - food_eaten)

if food_left >= food_eaten:
    print(f'{floor(diff)} kilos of food left.')
else:
    print(f'{ceil(diff)} more kilos of food are needed.')
