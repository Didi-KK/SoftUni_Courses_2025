group_budget = int(input())
season_of_the_year = input()
number_of_fisherman = int(input())

fishing_boat_rental = 0.00

if season_of_the_year == "Spring":
    fishing_boat_rental = 3_000.00
elif season_of_the_year == "Summer" or season_of_the_year == "Autumn":
    fishing_boat_rental = 4_200.00
elif season_of_the_year == "Winter":
    fishing_boat_rental = 2_600.00

discount = 0.00

if number_of_fisherman <= 6:
    discount = 0.10
elif number_of_fisherman <= 11:
    discount = 0.15
else:
    discount = 0.25

extra_discount = 0.00
if  number_of_fisherman % 2 == 0 and season_of_the_year != "Autumn":
    extra_discount = 0.05

total_boat_rental = fishing_boat_rental * (1 - discount) * (1 - extra_discount)
money_difference = group_budget - total_boat_rental

if group_budget >= total_boat_rental:
    print(f"Yes! You have {abs(money_difference):.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_difference):.2f} leva.")
