destroyed_ships_count = 0

rows = int(input())
ships = [list(map(int, input().split())) for _ in range(rows)]
coordinates_pair = input().split()

for coordinates in coordinates_pair:
    x, y = coordinates.split('-')
    if ships[int(x)][int(y)] > 0:
        ships[int(x)][int(y)] -= 1

        if ships[int(x)][int(y)] == 0:
            destroyed_ships_count += 1
            continue

print(destroyed_ships_count)
