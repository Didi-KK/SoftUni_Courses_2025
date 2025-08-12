def characters_in_range(first_char: str, second_char: str):


    characters_list = ""

    for char in range(ord(first_char) + 1, ord(second_char)):
        characters_list += chr(char) + " "

    return characters_list.strip()

starting_point = input()
ending_point = input()

print(characters_in_range(starting_point, ending_point))


