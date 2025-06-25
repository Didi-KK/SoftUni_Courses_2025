cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_length * cake_width
entry = input()

while entry != "STOP":
    
    cake_taken = int(entry)
    cake_pieces -= cake_taken
    
    if cake_pieces <= 0:
        break
    
    entry = input()

if cake_pieces >= 0:
    print(f'{cake_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
