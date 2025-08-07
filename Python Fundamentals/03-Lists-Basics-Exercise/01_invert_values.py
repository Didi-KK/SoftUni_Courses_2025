numbers_list = input().split(" ")

opposite_numbers = []

for current_number in numbers_list:
    current_number_as_integer = int(current_number)
    opposite_number = - current_number_as_integer
    opposite_numbers.append(opposite_number)

print(opposite_numbers)
