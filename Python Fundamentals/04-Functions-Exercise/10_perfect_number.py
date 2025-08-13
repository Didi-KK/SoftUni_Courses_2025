def is_perfect(some_number: int):
    divisors_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    if divisors_sum == some_number:
            return "We have a perfect number!"
    return "It's not so perfect."

my_number = int(input())
print(is_perfect(my_number))