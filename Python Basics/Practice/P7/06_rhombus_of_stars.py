rows = int(input())

for r in range(1, rows):
    print(f"{' ' * (rows - r)}*{' *' * (r - 1)}")
for r in range(1, rows + 1):
    print(f"{' ' * (r - 1)}*{' *' * (rows - r)}")