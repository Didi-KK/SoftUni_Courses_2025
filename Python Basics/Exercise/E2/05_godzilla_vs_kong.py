movie_budget = float(input())
extras = int(input())
costume_cost = float(input())
decor = movie_budget * 10 / 100

total_costume_cost = extras * costume_cost
if extras >= 150:
    total_costume_cost = extras * costume_cost * (1 - 10 / 100)
expenses = total_costume_cost + decor
money_difference = movie_budget - expenses
if movie_budget < expenses:
    print(f"Not enough money!")
    print(f"Wingard needs " f"{abs(money_difference):.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with " f"{abs(money_difference):.2f} leva left.")
