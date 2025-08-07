energy = 100
coins = 100
events = input().split("|")

for event in events:
    type_of_event, value = event.split("-")
    value = int(value)

    if type_of_event == "rest":

        current_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        gained_energy = energy - current_energy

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif type_of_event == "order":

        if energy >= 30:
            coins += value
            energy -= 30
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:

        if coins >= value:
            coins -= value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            exit()
print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")
