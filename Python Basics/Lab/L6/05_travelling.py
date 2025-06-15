while True:
    destination = input()
    if destination == 'End':
        break
    
    budget = float(input())
    total_amount = 0
    
    while total_amount < budget:
        amount = float(input())
        total_amount += amount
        
    print(f'Going to {destination}!')
 

