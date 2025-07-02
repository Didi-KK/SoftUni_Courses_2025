food_qty = int(input())
food_left = food_qty * 1000

command = input()
while command != 'Adopted':
    daily_ratio = int(command)
    food_left -= daily_ratio
    command = input()
    if command =='Adopted':
        break

if food_left >= 0:
    print(f'Food is enough! Leftovers: {food_left} grams.')
else:
    print(f'Food is not enough. You need {abs(food_left)} grams more.')

