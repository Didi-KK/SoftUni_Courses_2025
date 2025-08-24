treasure_chest = input().split("|")
stolen_items = []

while True:
    command = input()
    if command == "Yohoho!":
        break
    treasure_hunt = command.split()
    if treasure_hunt[0] == "Loot":
        items = treasure_hunt[1:]
        for item in items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif treasure_hunt[0] == "Drop":
        index = int(treasure_hunt[1])
        if index in range(len(treasure_chest)):

            item = treasure_chest.pop(index)
            treasure_chest.append(item)

    elif treasure_hunt[0] == "Steal":

        steal_loot_count = min(int(treasure_hunt[1]), len(treasure_chest))

        stolen_items = treasure_chest[-steal_loot_count:]
        treasure_chest = treasure_chest[: - steal_loot_count]
        print(", ".join(stolen_items))

if treasure_chest:
    treasure_gain = sum(len(elem) for elem in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {treasure_gain:.2f} pirate credits.")

else:
    print("Failed treasure hunt.")
