def even_numbers(numbers_as_string: str):
    numbers_as_string = numbers_as_string.split()
    numbers_as_digits =[]
    for num in numbers_as_string:
        numbers_as_digits.append(int(num))
    # number = list(map(int, numbers_as_string.split()))
    return list(filter(lambda x: x % 2 == 0, numbers_as_digits))

my_numbers = input()
print(even_numbers(my_numbers))