n = int(input())

counter = 0

for x1 in range(n+1):
    for x2 in range(n+1):
        for x3 in range(n+1):
            if (x1 + x2 + x3) == n:
                counter += 1
                break
print(counter)
