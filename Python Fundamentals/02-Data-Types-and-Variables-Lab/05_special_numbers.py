sum_digits = 0

integer = int(input())

for number in range(1, integer + 1):

    sum_digits = number
    if number > 10:
        sum_digits = number // 10 + number % 10
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")


