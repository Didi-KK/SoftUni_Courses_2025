values = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break
    elif command.startswith("swap"):
        index1, index2 = [int(elem) for elem in command.split()[1:]]
        values[index1], values[index2] = values[index2], values[index1]

    elif command.startswith("multiply"):
        index1, index2 = [int(elem) for elem in command.split()[1:]]

        values[index1] = values[index1] * values[index2]


    elif command.startswith("decrease"):
        values = [elem - 1 for elem in values]

print(", ".join(str(elem) for elem in values))
