number_of_strings = int(input())

key_word = input()
my_list = []

for new_string in range(number_of_strings):
    current_string = input()
    my_list.append(current_string)

print(my_list)

for i in range(len(my_list) - 1, -1, -1):
    element = my_list[i]
    if key_word not in element:
        my_list.remove(element)

print(my_list)
