def is_even(num):
    return num % 2 == 0
def is_prime(num):
    if num == 1:
        return False

    for divisor in range(2, num):
        if num % divisor == 0:
            return False

    return True

first_digit = int(input())
second_digit = int(input())
third_digit = int(input())
for num1 in range(1, first_digit + 1 ):
    for num2 in range(1, second_digit + 1 ):
        for num3 in range(1, third_digit + 1 ):
            if is_even(num1) and is_prime(num2) and is_even(num3):
                print(f'{num1} {num2} {num3}')
 