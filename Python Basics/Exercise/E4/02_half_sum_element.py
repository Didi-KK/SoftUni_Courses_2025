from sys import maxsize

n = int(input())

max_num = -maxsize
sum_numbers = 0

for _ in range(n):
    current_number = int(input())
    sum_numbers +=current_number
    
    if current_number > max_num:
        max_num = current_number
    continue
    
if max_num == sum_numbers - max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    sum_numbers -= max_num
    print('No')
    print(f'Diff = {abs(sum_numbers - max_num)}')
