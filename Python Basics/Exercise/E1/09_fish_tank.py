aquarium_length = int(input())
aquarium_width = int(input())
aquarium_height = int(input())
percent_decoration = float(input())

aquarium_capacity = (aquarium_length * aquarium_width * aquarium_height) / 1000
liters_capacity = aquarium_capacity * (1 - percent_decoration / 100)

print(liters_capacity)
