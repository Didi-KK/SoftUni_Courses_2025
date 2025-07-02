count = 0
luggage_size = 0
load_capacity = float(input())
capacity_left = load_capacity
while True:
    command = input()
    if command == 'End':
        print(f'Congratulations! All suitcases are loaded!')
        break
    if command != 'End':
        luggage_size = float(command)
        count += 1
        if count % 3 == 0:
            luggage_size *= 1.1
        if capacity_left <= luggage_size:
            count -= 1
            print(f'No more space!')
            break
        capacity_left -= luggage_size

print(f'Statistic: {count} suitcases loaded.')
