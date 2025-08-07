string_of_integer_numbers = input().split(" ")
count_of_numbers_to_remove = int(input())

list_ot_numbers = []

for number in string_of_integer_numbers:
    list_ot_numbers.append(int(number))

for to_delete_number in range(count_of_numbers_to_remove):
    smallest = min(list_ot_numbers)
    list_ot_numbers.remove(smallest)

modified_list_of_numbers = []

for num in list_ot_numbers:
    modified_list_of_numbers.append(str(num))

print(", ".join(modified_list_of_numbers))
