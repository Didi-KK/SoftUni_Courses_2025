number = int(input())

for num in range(1111, 10000):
    
    is_special = True
    num_as_string = str(num)
    
    for d in num_as_string:
        d_as_int = int(d)
        
        if d_as_int == 0:
            is_special = False
        elif number % d_as_int != 0:
            is_special = False
            break
    
    if is_special:
        print(num, end=' ')
