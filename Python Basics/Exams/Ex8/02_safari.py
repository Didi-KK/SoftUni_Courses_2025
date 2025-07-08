TOUR_GUIDE = 100
FUEL_PRICE = 2.10

budget = float(input())
fuel_liters = float(input())
week_day = input()

expenses = fuel_liters * FUEL_PRICE + TOUR_GUIDE
if week_day == 'Saturday':
    expenses *= 0.90
elif week_day == 'Sunday':
    expenses *= 0.80

diff = budget - expenses

if diff >= 0:
    print(f'Safari time! Money left: {diff:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {abs(diff):.2f} lv.')
