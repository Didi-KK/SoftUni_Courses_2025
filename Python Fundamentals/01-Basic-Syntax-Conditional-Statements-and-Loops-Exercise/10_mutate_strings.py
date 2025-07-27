# You will be given two strings.
# Transform the first string into the second one,
# letter by letter, starting from the first one.
# After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.
first_text = input()
second_text = input()

current = list(first_text)
seen = set()
unique=()
for letter_index in range(len(first_text)):
    if current[letter_index] != second_text[letter_index]:
        current[letter_index] = second_text[letter_index]
        unique = ''.join(current)
        if unique not in seen:
            print(unique)
            seen.add(unique)
