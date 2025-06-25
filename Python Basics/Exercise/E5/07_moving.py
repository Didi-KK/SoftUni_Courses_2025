space_width = int(input())
space_length = int(input())
space_height = int(input())

space_capacity = space_width * space_length * space_height

entry = input()

while entry != 'Done':
    
    space_taken = int(entry)
    space_capacity -= space_taken
    
    if space_capacity <= 0:
        break
        
    entry = input()
    
if space_capacity >= 0:
    print(f'{space_capacity} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(space_capacity)} Cubic meters more.')
    

