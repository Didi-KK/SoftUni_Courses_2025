neighborhood = list(map(int, input().split("@")))
house_index = 0
house_visited = []
command = input()
while command != "Love!":

    length = int(command.split()[1])
    house_index += length
    if house_index in house_visited:
        print(f"Place {house_index} already had Valentine's day.")
        command = input()
        continue
    if house_index in range(len(neighborhood)):

        neighborhood[house_index] -= 2
        if neighborhood[house_index] == 0:
            house_visited.append(house_index)
            print(f"Place {house_index} has Valentine's day.")

    else:
        house_index = 0
        if house_index in house_visited:
            print(f"Place {house_index} already had Valentine's day.")
            command = input()
            continue
        neighborhood[house_index] -= 2
        if neighborhood[house_index] == 0:
            house_visited.append(house_index)
            print(f"Place {house_index} has Valentine's day.")
            command = input()
            continue

    command = input()

print(f"Cupid's last position was {house_index}.")
missed_houses = sum(1 for hearts in neighborhood if hearts > 0)

if missed_houses > 0:
    print(f"Cupid has failed {missed_houses} places.")
else:
    print("Mission was successful.")
