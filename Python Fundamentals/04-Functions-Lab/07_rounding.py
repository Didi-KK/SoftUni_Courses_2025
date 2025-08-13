def round_numbers(numbers_as_string):
    numbers = numbers_as_string.split()
    return  [round(float(number)) for number in numbers]


current_number_string = input()

print(round_numbers(current_number_string))