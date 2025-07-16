game_rounds = int(input())

invalid_num = 0
num9 = 0
num19 = 0
num29 = 0
num39 = 0
num50 = 0
points = 0.0

for i in range(game_rounds):
    number = int(input())
    if number < 0:
        invalid_num += 1
        points /= 2
    elif number <= 9:
        num9 += 1
        points += number * 0.2
    elif number <= 19:
        num19 += 1
        points += number * 0.3
    elif number <= 29:
        num29 += 1
        points += number * 0.40
    elif number <= 39:
        num39 += 1
        points += 50
    elif number <= 50:
        num50 += 1
        points += 100
    elif number > 50:
        invalid_num += 1
        points /= 2

num9_p = num9 / game_rounds * 100
num19_p = num19 / game_rounds * 100
num29_p = num29 / game_rounds * 100
num39_p = num39 / game_rounds * 100
num50_p = num50 / game_rounds * 100
invalid_num_p = invalid_num / game_rounds * 100

print(f'{points:.2f}\nFrom 0 to 9: {num9_p:.2f}%'
      f'\nFrom 10 to 19: {num19_p:.2f}%'
      f'\nFrom 20 to 29: {num29_p:.2f}%'
      f'\nFrom 30 to 39: {num39_p:.2f}%'
      f'\nFrom 40 to 50: {num50_p:.2f}%'
      f'\nInvalid numbers: {invalid_num_p:.2f}%')
