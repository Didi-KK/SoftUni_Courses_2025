initial_energy = int(input())
command = input()
energy_left = initial_energy
won_battles = 0
while initial_energy > 0:
    if command == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {energy_left}")
        break
    distance_of_an_enemy = int(command)
    if energy_left >= distance_of_an_enemy:
        energy_left -= distance_of_an_enemy
        won_battles += 1
        if won_battles % 3 == 0:
            energy_left += won_battles
        command = input()
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy_left} energy")
        break
