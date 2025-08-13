def orders(product, quantity):
    if product == "coffee":
        return 1.50 * quantity
    elif product == "water":
        return 1.00 * quantity
    elif product == "coke":
        return 1.40 * quantity
    elif product == "snacks":
        return 2.00 * quantity


current_product = input()
qty = int(input())

amount = orders(current_product, qty)
print(f"{amount:.2f}")
