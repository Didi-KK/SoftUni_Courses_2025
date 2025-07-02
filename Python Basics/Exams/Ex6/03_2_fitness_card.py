price = 0
sport_choice = ''
budget = float(input())
sex = input()
age = int(input())
sport = input()
if sex == 'f':
    if sport == 'Gym':
        sport_choice = sport
        price = 35
    elif sport == 'Boxing':
        sport_choice = sport
        price = 37
    elif sport == 'Yoga':
        sport_choice = sport
        price = 42
    elif sport == 'Zumba':
        sport_choice = sport
        price = 31
    elif sport == 'Dances':
        sport_choice = sport
        price = 53
    elif sport == 'Pilates':
        sport_choice = sport
        price = 37
elif sex == 'm':
    if sport == 'Gym':
        sport_choice = sport
        price = 42
    elif sport == 'Boxing':
        sport_choice = sport
        price = 41
    elif sport == 'Yoga':
        sport_choice = sport
        price = 45
    elif sport == 'Zumba':
        sport_choice = sport
        price = 34
    elif sport == 'Dances':
        sport_choice = sport
        price = 51
    elif sport == 'Pilates':
        sport_choice = sport
        price = 39
if age <= 19:
    price *= 0.80

if price <= budget:
    print(f'You purchased a 1 month pass for {sport_choice}.')
else:
    money_short = price - budget
    print(f'You don\'t have enough money! You need ${money_short:.2f} more.')
