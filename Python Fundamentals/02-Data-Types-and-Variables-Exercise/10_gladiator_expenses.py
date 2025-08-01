total_expenses = 0
shield_count = 0

lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
for lost_game in range(1, lost_fights_count + 1):

    if lost_game % 2 == 0:
        total_expenses += helmet_price

    if lost_game % 3 == 0:
        total_expenses += sword_price
        if lost_game % 2 == 0:
            total_expenses += shield_price
            shield_count += 1
            if shield_count % 2 == 0:
                total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")

