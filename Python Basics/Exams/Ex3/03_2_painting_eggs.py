egg_size = input()
egg_color = input()
bundle = int(input())

bundle_price = 0

if egg_size == 'Large':
    if egg_color == 'Red':
        bundle_price = 16
    elif egg_color == 'Green':
        bundle_price = 12
    elif egg_color == 'Yellow':
        bundle_price = 9

elif egg_size == 'Medium':
    if egg_color == 'Red':
        bundle_price = 13
    elif egg_color == 'Green':
        bundle_price = 9
    elif egg_color == 'Yellow':
        bundle_price = 7

elif egg_size == 'Small':
    if egg_color == 'Red':
        bundle_price = 9
    elif egg_color == 'Green':
        bundle_price = 8
    elif egg_color == 'Yellow':
        bundle_price = 5

total_price = bundle * bundle_price
production_cost = 0.35 * total_price
profit = total_price - production_cost
print(f'{profit:.2f} leva.')
