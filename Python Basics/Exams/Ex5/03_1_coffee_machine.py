total_price = 0
price = 0

drink = input()
drink_extras = input()
drink_qty = int(input())

if drink =='Espresso':
    if drink_extras == 'Without':
        price = 0.90
        price *= 0.65
    elif drink_extras == 'Normal':
        price = 1.00
    elif drink_extras == 'Extra':
        price = 1.20
    if drink_qty >= 5:
        price *= 0.75

elif drink =='Cappuccino':
    if drink_extras == 'Without':
        price = 1.00
        price *= 0.65
    elif drink_extras == 'Normal':
        price = 1.20
    elif drink_extras == 'Extra':
        price = 1.60

elif drink == 'Tea':
    if drink_extras == 'Without':
        price = 0.50
        price *= 0.65
    elif drink_extras == 'Normal':
        price = 0.60
    elif drink_extras == 'Extra':
        price = 0.70

total_price = drink_qty * price
if total_price > 15.00:
    total_price *= 0.80

print(f'You bought {drink_qty} cups of {drink} for {total_price:.2f} lv.')
