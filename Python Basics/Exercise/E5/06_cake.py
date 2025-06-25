cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_length * cake_width

while cake_pieces > 0:
    entry = input()
    
    if entry != 'STOP':
        cake_taken = int(entry)
        cake_pieces -= cake_taken
        if cake_pieces <= 0:
            print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
            break
    elif entry == 'STOP':
        print(f'{cake_pieces} pieces are left.')
        break
