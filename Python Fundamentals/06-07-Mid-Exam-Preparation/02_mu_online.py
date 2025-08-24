MAX_HEALTH = 100
health = MAX_HEALTH
bitcoins = 0

rooms = input().split('|')

for i in range(len(rooms)):
    action, value = rooms[i].split()
    value = int(value)

    if action == "potion":
        healed = min(value, MAX_HEALTH - health)
        health += healed
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif action == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")

    else:
        health -= value

        if health > 0:
            print(f"You slayed {action}.")
        else:
            print(f"You died! Killed by {action}.\nBest room: {i + 1}")
            break
else:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
