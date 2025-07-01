hearthstone_qty = 0
fornite_qty = 0
overwatch_qty = 0
others_qty = 0

games_qty = int(input())
for _ in range(games_qty):
    command = input()
    if command == 'Hearthstone':
        hearthstone_qty += 1
    elif command == 'Fornite':
        fornite_qty += 1
    elif command == 'Overwatch':
        overwatch_qty += 1
    else:
        others_qty += 1

hearthstone_percentage = (hearthstone_qty / games_qty) * 100
fornite_percentage = (fornite_qty / games_qty) * 100
overwatch_percentage = (overwatch_qty / games_qty) * 100
others_percentage = (others_qty / games_qty) * 100

print(f'Hearthstone - {hearthstone_percentage:.2f}%')
print(f'Fornite - {fornite_percentage:.2f}%')
print(f'Overwatch - {overwatch_percentage:.2f}%')
print(f'Others - {others_percentage:.2f}%')
