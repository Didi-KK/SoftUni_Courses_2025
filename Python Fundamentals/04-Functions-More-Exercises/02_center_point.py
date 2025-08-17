def hypotenuse(a: float, b: float):
    from math import sqrt
    return sqrt(abs(a**2) + abs(b**2))

from math import floor
x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

c_1 = hypotenuse(a=x_1, b=y_1)
c_2 = hypotenuse(a=x_2, b=y_2)

if c_1 <= c_2:
    print(f"({floor(x_1)}, {floor(y_1)})")
else:
    print(f"({floor(x_2)}, {floor(y_2)})")



