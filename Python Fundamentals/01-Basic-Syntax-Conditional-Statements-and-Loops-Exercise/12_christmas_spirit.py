money_spent = 0
xmas_spirit = 0

decorations_qty = int(input())
days_until_xmas = int(input())

if days_until_xmas % 10 == 0:
    xmas_spirit -= 30

for day in range(1, days_until_xmas + 1):

    if day % 11 == 0:
        decorations_qty += 2

    if day % 2 == 0:
        money_spent += decorations_qty * 2
        xmas_spirit += 5

    if day % 3 == 0:
        money_spent += decorations_qty * 5
        xmas_spirit += 3
        money_spent += decorations_qty * 3
        xmas_spirit += 10
        if day % 5 == 0:
            xmas_spirit += 30

    if day % 5 == 0:
        money_spent += decorations_qty * 15
        xmas_spirit += 17

    if day % 10 == 0:
        xmas_spirit -= 20
        money_spent += 5
        money_spent += 3
        money_spent += 15

print(f"Total cost: {money_spent}")
print(f"Total spirit: {xmas_spirit}")
