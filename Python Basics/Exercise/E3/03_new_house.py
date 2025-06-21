flower_type = input()
flower_qty = int(input())
budget = int(input())

flower_price = 0.00
discount = 0.00

if flower_type == "Roses":
    flower_price = 5.00
    if 80 < flower_qty:
        discount = 0.10

elif flower_type == "Dahlias":
    flower_price = 3.80
    if 90 < flower_qty:
        discount = 0.15

elif flower_type == "Tulips":
    flower_price = 2.80
    if 80 < flower_qty:
        discount = 0.15

elif flower_type == "Narcissus":
    flower_price = 3.00
    if 120 > flower_qty:
        discount = -0.15

elif flower_type == "Gladiolus":
    flower_price = 2.50
    if 80 > flower_qty:
        discount = -0.20

total_price = flower_qty * flower_price * (1 - discount)
money_difference = budget - total_price

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_qty} {flower_type} "
          f"and {abs(money_difference):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(money_difference):.2f} leva more.")
