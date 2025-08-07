fire = input().split("#")
water = int(input())

valid_cells = []
effort = 0
total_fire = 0

for index in range(len(fire)):

    type_of_fire, value_of_cell = fire[index].split(" = ")
    value_of_cell = int(value_of_cell)

    if type_of_fire == 'High' and value_of_cell in range(81, 126):
        if water < value_of_cell:
            continue
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        valid_cells.append(value_of_cell)

    elif type_of_fire == 'Medium' and value_of_cell in range(51, 81):
        if water < value_of_cell:
            continue
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        valid_cells.append(value_of_cell)

    elif type_of_fire == 'Low' and value_of_cell in range(1, 51):
        if water < value_of_cell:
            continue
        water -= value_of_cell
        effort += value_of_cell * 0.25
        total_fire += value_of_cell
        valid_cells.append(value_of_cell)

print(f"Cells:")
for cell in valid_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
