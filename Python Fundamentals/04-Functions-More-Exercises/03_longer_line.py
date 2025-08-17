def hypotenuse(a: float, b: float):
    from math import sqrt
    return sqrt(abs(a**2) + abs(b**2))
from math import floor
x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())
c_12 = hypotenuse(a=(x_1-x_2), b=(y_1-y_2))
c_34 = hypotenuse(a=(x_3-x_4), b=(y_3-y_4))
c_1 = (hypotenuse(x_1, y_1))
c_2 = (hypotenuse(x_2, y_2))
c_3 = (hypotenuse(x_3, y_3))
c_4 = (hypotenuse(x_4, y_4))
if c_12 >= c_34:
    if c_1 <= c_2:
        print(f"({floor(x_1)}, {floor(y_1)})({floor(x_2)}, {floor(y_2)})")
    else:
        print(f"({floor(x_2)}, {floor(y_2)})({floor(x_1)}, {floor(y_1)})")
else:
    if c_3 <= c_4:
        print(f"({floor(x_3)}, {floor(y_3)})({floor(x_4)}, {floor(y_4)})")
    else:
        print(f"({floor(x_4)}, {floor(y_4)})({floor(x_3)}, {floor(y_3)})")