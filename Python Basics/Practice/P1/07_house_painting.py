# House height
while True:
    x = float(input())
    if 2.00 <= x <= 100.00:
        break
# House length
while True:
    y = float(input())
    if 2.00 <= y <= 100.00:
        break
# House height
while True:
    h = float(input())
    if 2.00 <= h <= 100.00:
        break
# Front and back walls are squares with side length x
front_wall_area = float(x * x)
back_wall_area = float(x * x)

# On the front wall there is a door, rectangle with sizes w=1.2m and h=2m
door_area = float(1.20 * 2.00)

# The two (2) side walls are rectangles with sides "x" and "y" with square window on both with side 1.5m
side_wall_area = float(x * y)
window_area = float(1.50 * 1.50)

# The roof has two (2) rectangle sides "x" and "y" and teo (2) equilateral triangles with side "x" and height "h"
roof_rectangle_area = float(x * y)
roof_triangle_area = float((x * h) / 2)

# Paint usage - walls - green paint is 1 liter for 3.4 m2, roof - red paint – 1 liter for 4.3 m2.

walls_green_paint_l_per_sq_m = 3.40
roof_red_paint_l_per_sq_m = 4.30

total_walls_sq_m = float(2 * front_wall_area + 2 * side_wall_area - 1 * door_area - 2 * window_area)
total_roof_sq_m = float(2 * roof_rectangle_area + 2 * roof_triangle_area)

total_green_paint_l = float(total_walls_sq_m / walls_green_paint_l_per_sq_m)
total_red_paint_l = float(total_roof_sq_m / roof_red_paint_l_per_sq_m)

print(f'{total_green_paint_l:.2f}')
print(f'{total_red_paint_l:.2f}')
