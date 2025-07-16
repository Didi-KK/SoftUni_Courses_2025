inheritance = float(input())
to_year = int(input())

money_left = inheritance
ivan_age = 18
for i in range(1800, to_year + 1):
    if i % 2 == 0:
        money_left -= 12_000
    else:
        money_left -= (12_000 + ivan_age * 50)
    ivan_age += 1

if money_left >= 0:
    print(f'Yes! He will live a carefree life and will have {money_left:.2f} dollars left.')
else:
    print(f'He will need {abs(money_left):.2f} dollars to survive.')