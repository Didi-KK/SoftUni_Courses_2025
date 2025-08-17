def product_of_three(a: int, b: int, c: int) -> str:
    if a == 0 or b == 0 or c == 0:
        return "zero"

    count_negative = 0
    for n in (a, b, c):
        if n < 0:
            count_negative += 1
    if count_negative % 2 == 0:
        return "positive"
    else:
        return "negative"

first_number = int(input())
second_number = int(input())
third_number = int(input())
print(product_of_three(a=first_number, b=second_number, c=third_number))
