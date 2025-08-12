def odd_and_even_sum(number: int):

    even_sum = 0
    odd_sum = 0
    while number > 0:
        current_number = number % 10
        if current_number % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number
        number //= 10

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

my_number = int(input())
odd_and_even_sum(my_number)