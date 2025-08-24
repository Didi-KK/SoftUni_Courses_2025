groceries = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break

    elif command.startswith("Urgent"):
        item = command.split()[1]
        if item in groceries:
            continue
        groceries.insert(0, item)

    elif command.startswith("Unnecessary"):
        item = command.split()[1]
        if item not in groceries:
            continue
        groceries.remove(item)

    elif command.startswith("Correct"):
        old_item, new_item = command.split()[1:]
        if old_item not in groceries:
            continue
        index = groceries.index(old_item)
        groceries[index] = new_item

    elif command.startswith("Rearrange"):
        item = command.split()[1]
        if item not in groceries:
            continue
        index = groceries.index(item)
        groceries.remove(item)
        groceries.append(item)

print(', '.join(groceries))
