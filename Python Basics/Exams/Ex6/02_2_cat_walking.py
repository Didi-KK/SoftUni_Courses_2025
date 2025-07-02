min_walk = int(input())
num_walks = int(input())
daily_calories = int(input())
burned_calories = num_walks * min_walk * 5

if burned_calories >= daily_calories / 2:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.')
