numbers_count = int(input())

numbers_sum = 0

average_sum = 0

for i in range(numbers_count):
    number = int(input())
    numbers_sum += number
    average_sum = numbers_sum / numbers_count

print(f'{average_sum:.2f}')
