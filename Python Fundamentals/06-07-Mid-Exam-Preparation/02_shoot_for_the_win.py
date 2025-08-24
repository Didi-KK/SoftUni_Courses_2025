targets = list(map(int, input().split()))

shots_counter = 0

while True:
    command = input()
    if command == "End":
        break
    index = int(command)

    if index in range(len(targets)) and targets[index] != -1:
        shot_value = targets[index]
        shots_counter += 1
        targets[index] = -1

        for idx in range(len(targets)):
            if targets[idx] == -1:
                continue
            if targets[idx] > shot_value:
                targets[idx] -= shot_value
            else:
                targets[idx] += shot_value
print(f"Shot targets: {shots_counter} -> {' '.join(str(elem) for elem in targets)}")