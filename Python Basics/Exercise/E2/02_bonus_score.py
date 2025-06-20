number = int(input())
if number <= 100:
    bonus_points = 5
elif number > 1000:
    bonus_points = number * 10 / 100
else:
    bonus_points = number * 20 / 100

if number % 2 == 0:
    bonus_points += 1
elif number % 10 == 5:
    bonus_points += 2

final_number = number + bonus_points

print(bonus_points)
print(final_number)
