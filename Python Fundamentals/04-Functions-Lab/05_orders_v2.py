def orders(product, quantity):
    return {
        "coffee": 1.50 * quantity,
        "water": 1.00 * quantity,
        "coke":1.40 * quantity,
        "snacks":2.00 * quantity
    }.get(product)


current_product = input()
qty = int(input())

amount = orders(current_product, qty)
print(f"{amount:.2f}")