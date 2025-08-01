water_tank_capacity = 255

times_to_add_water = int(input())

for every_fill_water in range(times_to_add_water):
    liters = int(input())
    if water_tank_capacity < liters:
        print("Insufficient capacity!")
        continue
    water_tank_capacity -= liters

print(255 - water_tank_capacity)