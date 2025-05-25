from math import pi

figure = input()
area = 0
if figure == "square":
    side = float(input())
    area = side ** 2
if figure == "rectangle":
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
if figure == "circle":
    radius = float(input())
    area = pi * radius ** 2
if figure == "triangle":
    triangle_side = float(input())
    height_to_side = float(input())
    area = triangle_side * height_to_side / 2
print(f'{area:.3f}')
