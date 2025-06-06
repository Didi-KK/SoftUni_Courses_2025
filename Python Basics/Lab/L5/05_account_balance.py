account_available_sum = 0

while True:
    text = input()
    if text == 'NoMoreMoney':
        break
    
    current_sum = float(text)
    
    if current_sum >= 0:
        account_available_sum += current_sum
        print(f'Increase: {current_sum:.2f}')
    else:
        print(f'Invalid operation!')
        break
        
print(f'Total: {account_available_sum:.2f}')
        
        
        
    
    