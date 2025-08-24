targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break
    if command.startswith("Shoot"):
        index, power = [int(elem) for elem in command.split()[1:]]
        if index in range(len(targets)):
            targets[index] = targets[index] - power
            if targets[index] <= 0:
                targets.pop(index)

    elif command.startswith("Add"):
        index, value = [int(elem) for elem in command.split()[1:]]
        if index in range(len(targets)):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command.startswith("Strike"):
        index, radius = [int(elem) for elem in command.split()[1:]]
        if (index in range(len(targets))
                and (index + radius) in range(len(targets))
                and (index - radius) in range(len(targets))):
            del targets[(index - radius):(index + radius + 1)]
        else:
            print("Strike missed!")

print('|'.join(str(elem) for elem in targets))
