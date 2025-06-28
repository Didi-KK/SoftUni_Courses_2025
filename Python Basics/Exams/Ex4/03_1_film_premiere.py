# Напишете програма, която изчислява цената, която трябва да се заплати,
# като имате в предвид следните отстъпки:
# При избран филм "Star Wars" и закупени поне четири билета, има 30% семейна отстъпка.
# При избран филм "Jumanji" и закупени точно два билета, има 15% отстъпка за двама.

movie_title = input()
snack = input()
tickets = int(input())
price = 0

total_expenses = tickets * price

if movie_title == 'John Wick':
    if snack == 'Drink':
        price = 12.00
    elif snack == 'Popcorn':
        price = 15.00
    elif snack == 'Menu':
        price = 19.00

if movie_title == 'Star Wars':
    if snack == 'Drink':
        price = 18.00
    elif snack == 'Popcorn':
        price = 25.00
    elif snack == 'Menu':
        price = 30.00

if movie_title == 'Jumanji':
    if snack == 'Drink':
        price = 9.00
    elif snack == 'Popcorn':
        price = 11.00
    elif snack == 'Menu':
        price = 14.00

total_expenses = tickets * price
if movie_title == 'Star Wars' and tickets >= 4:
    total_expenses *= 0.70
if movie_title == 'Jumanji' and tickets == 2:
    total_expenses *= 0.85

print(f'Your bill is {total_expenses:.2f} leva.')
