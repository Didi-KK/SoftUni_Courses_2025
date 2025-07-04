from math import floor

#  Ако топката е “black” точките ни се делят на 2, като закръгляме към по-малкото цяло число.
# Ако топката е с какъвто и да е цвят, различен от по-горните, точките не се манипулират и
# програмата продължава да работи.
total_points = 0
red_balls = 0  # 5
orange_balls = 0  # 10
yellow_balls = 0  # 15
white_balls = 0  # 20
black_balls = 0
other_balls = 0
balls_qty = int(input())
for _ in range(balls_qty):
    color = input()
    if color == 'red':
        red_balls += 1
        total_points += 5
    elif color == 'orange':
        orange_balls += 1
        total_points += 10
    elif color == 'yellow':
        yellow_balls += 1
        total_points += 15
    elif color == 'white':
        white_balls += 1
        total_points += 20
    elif color == 'black':
        black_balls += 1
        total_points = floor(total_points / 2)
    else:
        other_balls += 1

print(f'Total points: {total_points}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_balls}')
print(f'Divides from black balls: {black_balls}')
