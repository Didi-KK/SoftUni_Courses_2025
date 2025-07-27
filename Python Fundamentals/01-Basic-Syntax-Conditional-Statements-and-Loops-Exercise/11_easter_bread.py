loaves = 0
colored_eggs = 0

budget = float(input())
flour_kg_price = float(input())
money_left = budget
egg_pack_price = 0.75 * flour_kg_price
milk_l_price = 1.25 * flour_kg_price

loaf_cost = 1 * egg_pack_price + 1 * flour_kg_price + 0.250 * milk_l_price

while money_left > loaf_cost:
    loaves += 1
    colored_eggs += 3
    money_left -= loaf_cost
    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
