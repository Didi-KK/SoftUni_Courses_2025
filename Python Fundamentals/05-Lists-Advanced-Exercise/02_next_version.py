previous_version = [int(digit) for digit in input().split('.')]

previous_version[-1] += 1

for index in range(len(previous_version) -1, 0, -1):
    if previous_version[index] > 9:
        previous_version[index] = 0
        previous_version[index-1] += 1
next_version = '.'.join([str(digit) for digit in previous_version])

print(next_version)