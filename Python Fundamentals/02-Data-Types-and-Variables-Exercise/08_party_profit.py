from math import floor
daily_earnings = 0
total_earnings = 0
group_size = int(input())
days_of_adventure = int(input())

for day in range(1, days_of_adventure + 1):

    daily_earnings += 50
    daily_earnings -= group_size * 2

    if day % 10 == 0:
        group_size -= 2
        daily_earnings += 2 * 2
    if day % 15 == 0:
        group_size += 5
        daily_earnings -= 5 * 2

    if day % 3 == 0:
        daily_earnings -= group_size * 3

    if day % 5 == 0:
        daily_earnings += group_size * 20
        if day % 3 == 0:
            daily_earnings -= group_size * 2

    total_earnings += daily_earnings
    daily_earnings = 0


companion_coins = floor(total_earnings / group_size)
print(f"{group_size} companions received {companion_coins} coins each.")

