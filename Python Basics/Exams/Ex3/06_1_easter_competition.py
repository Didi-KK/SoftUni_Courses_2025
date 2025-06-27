most_points = 0
best_baker = ''
baker_name = ''
baker_points = 0

easter_bread = int(input())

for n in range(easter_bread):
    baker_points = 0
    baker_name = input()
    command = input()
    while command != 'Stop':
        visitor_points = int(command)
        baker_points += visitor_points
        command = input()
    if command == 'Stop':
        print(f'{baker_name} has {baker_points} points.')
        if baker_points > most_points:
            most_points = baker_points
            best_baker = baker_name
            print(f'{baker_name} is the new number 1!')

            continue
        continue
    continue

print(f'{best_baker} won competition with {most_points} points!')
