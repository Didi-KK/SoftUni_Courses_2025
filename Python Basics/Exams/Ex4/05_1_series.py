budget = float(input())
series = int(input())

budget_left = budget

for _ in range(series):
    title = input()
    price = float(input())
    if title == 'Thrones':
        price *= 0.5
    elif title == 'Lucifer':
        price*= 0.6
    elif title == 'Protector':
        price *= 0.7
    elif title == 'TotalDrama':
        price *= 0.8
    elif title == 'Area':
        price *= 0.9

    budget_left -= price

if budget_left >= 0:
    print(f'You bought all the series and left with {abs(budget_left):.2f} lv.')
else:
    print(f'You need {abs(budget_left):.2f} lv. more to buy the series!')
