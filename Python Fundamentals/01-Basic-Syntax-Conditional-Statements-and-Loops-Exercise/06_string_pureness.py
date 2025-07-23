exclude_chars = [",", ".", "_"]

number_of_strings = int(input())

for new_string in range(number_of_strings):
    string = input()
    if any(char in string for char in exclude_chars):
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')
