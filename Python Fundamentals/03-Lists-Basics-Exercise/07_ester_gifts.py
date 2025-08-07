easter_gifts = input().split()
new_orders = []

command = input()
while command != "No Money":
    new_orders = command.split()

    if "OutOfStock" in new_orders:
        easter_gifts_new = []
        for word in easter_gifts:
            new_element = word.replace(new_orders[1], "None")
            easter_gifts_new.append(new_element)
            easter_gifts = easter_gifts_new

    elif "Required" in new_orders:
        if 0 <= int(new_orders[2]) <= len(easter_gifts) - 1:
            easter_gifts[int(new_orders[2])] = new_orders[1]

    elif "JustInCase" in new_orders:
            easter_gifts[-1] = new_orders[1]

    command = input()

for i in range(len(easter_gifts) - 1, -1, -1):
    if "None" in easter_gifts:
        easter_gifts.remove("None")

print(" ".join(easter_gifts))
