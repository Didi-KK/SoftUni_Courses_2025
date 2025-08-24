def valid_index(index, entry_data):
    return index in range(0, len(entry_data))


pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
maximum_health_capacity = int(input())
need_repair = maximum_health_capacity * 0.20

while True:

    command = input()

    if command == "Retire":
        print(f"Pirate ship status: {sum(pirate_ship)}")
        print(f"Warship status: {sum(warship)}")
        break

    elif command.startswith("Fire"):
        idx, damage = [int(elem) for elem in command.split()[1:]]

        if not valid_index(idx, warship):
            continue

        warship[idx] -= damage
        if warship[idx] <= 0:
            print("You won! The enemy ship has sunken.")
            break

    elif command.startswith("Defend"):
        start_idx, end_idx, damage = [int(elem) for elem in command.split()[1:]]

        if not (valid_index(start_idx, pirate_ship) and valid_index(end_idx, pirate_ship)):
            continue

        for idx in range(start_idx, end_idx + 1):
            pirate_ship[idx] -= damage
            if pirate_ship[idx] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()

    elif command.startswith("Repair"):
        idx, health = [int(elem) for elem in command.split()[1:]]

        if not valid_index(idx, pirate_ship):
            continue

        pirate_ship[idx] += min(health, maximum_health_capacity - pirate_ship[idx])

    elif command == "Status":

        for_repair = sum(1 for section in pirate_ship if section < need_repair)
        print(f"{for_repair} sections need repair.")
