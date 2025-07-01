cocktail_price = 0
turnover = 0
is_party = False
target_profit = float(input())
command = input()
while command != 'Party':
    cocktail = command
    cocktail_qty = int(input())
    cocktail_price = len(cocktail)
    order_price = cocktail_price * cocktail_qty
    if order_price % 2 != 0:
        order_price *= 0.75
    turnover += order_price
    if turnover >= target_profit:
        break
    command = input()
    if command == 'Party!':
        is_party = True
        break
diff = target_profit - turnover
if is_party:
    print(f'We need {abs(diff):.2f} leva more.')
else:
    print(f'Target acquired.')
print(f'Club income - {turnover:.2f} leva.')
