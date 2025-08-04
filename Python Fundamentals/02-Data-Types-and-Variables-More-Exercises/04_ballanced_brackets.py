number_of_lines = int(input())

is_balanced = True
is_opened = False

for lines in range(number_of_lines):
    line = input()

    if line == '(':
        if is_opened:
            is_balanced = False
            break
        is_opened = True
    elif line == ')':
        if not is_opened:
            is_balanced = False
            break
        is_opened = False

if is_opened:
    is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")