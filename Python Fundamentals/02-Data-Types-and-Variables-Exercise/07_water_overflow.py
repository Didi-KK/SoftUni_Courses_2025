water_tank_capacity = 255

times_to_add_water = int(input())

water_tank_filled = 0

for every_fill_water in range(times_to_add_water):
    liters = int(input())

    if water_tank_filled < water_tank_capacity:
        water_tank_filled += liters
    if water_tank_filled > water_tank_capacity:
        water_tank_filled -= liters
        if water_tank_filled < water_tank_capacity:
            print("Insufficient capacity!")
    if water_tank_filled == water_tank_capacity:
        break

print(water_tank_filled)






