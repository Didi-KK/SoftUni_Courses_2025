sum_prime_numbers = 0
sum_non_prime_numbers = 0

while True:
    
    entry_data = input()
    if entry_data == 'stop':
        break
    
    number = int(entry_data)
    if number < 0:
        print(f'Number is negative.')
        continue
    is_prime = True
    
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        sum_prime_numbers += number
    else:
        sum_non_prime_numbers += number

print(f'Sum of all prime numbers is: {sum_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_non_prime_numbers}')
