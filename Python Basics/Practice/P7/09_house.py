house_size = int(input())

roof_size = (house_size + 1) // 2

stars = 2 if house_size % 2 == 0 else 1

for r in range(roof_size):
    row = f"{'-' * ((house_size - stars) // 2)}{'*' * stars}{'-' * ((house_size - stars) // 2)}"
    stars += 2
    print(row)
base_size = house_size - roof_size
for r in range(base_size):
    row = f"|{'*' * (house_size - 2)}|"
    print(row)