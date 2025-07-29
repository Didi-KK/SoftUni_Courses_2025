animals = input()
my_animals = animals.split(", ")
my_animals.reverse()

wolf_position = my_animals.index("wolf")

if wolf_position == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!")