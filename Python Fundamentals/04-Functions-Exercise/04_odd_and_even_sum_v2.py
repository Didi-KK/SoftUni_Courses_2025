def odd_and_even_sum(number: str):

    even_sum = 0
    odd_sum = 0

    for digit in number:

        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")

my_number = input()
odd_and_even_sum(my_number)