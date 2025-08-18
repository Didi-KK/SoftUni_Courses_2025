number = 0
total_sum = 0

distances = [int(number) for number in input().split()]

while True:
    if not distances:
        break

    idx = int(input())

    if idx < 0:

        number = distances[0]
        distances.pop(0)
        distances.insert(0, distances[-1])

    elif idx not in range(len(distances)):

        number = distances[-1]
        distances.pop(-1)
        distances.append(distances[0])

    else:
        number = distances[idx]
        distances.pop(idx)

    total_sum += number

    for i in range(len(distances)):
        if distances[i] <= number:
            distances[i] += number
        else:
            distances[i] -= number
            
print(total_sum)
