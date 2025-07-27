while True:
    string = input()
    if string == 'End':
        break
    elif string == 'SoftUni':
        continue

    doubled = ''.join(char * 2 for char in string)
    print(doubled)
