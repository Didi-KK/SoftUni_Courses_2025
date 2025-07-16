load_number = int(input())

microbus_cost = 0
truck_cost = 0
train_cost = 0

microbus_tonnage = 0
truck_tonnage = 0
train_tonnage = 0

for i in range(load_number):
    load_tonnage = int(input())
    if load_tonnage <= 3:
        microbus_tonnage += load_tonnage
        microbus_cost += load_tonnage * 200
    elif load_tonnage <= 11:
        truck_tonnage += load_tonnage
        truck_cost += load_tonnage * 175
    else:
        train_tonnage += load_tonnage
        train_cost += load_tonnage * 120

total_tonnage = microbus_tonnage + truck_tonnage + train_tonnage
average_cost = (microbus_cost + truck_cost + train_cost) / total_tonnage
microbus_p = microbus_tonnage / total_tonnage * 100
truck_p = truck_tonnage / total_tonnage * 100
train_p = train_tonnage / total_tonnage * 100

print(f'{average_cost:.2f}'
      f'\n{microbus_p:.2f}%'
      f'\n{truck_p:.2f}%'
      f'\n{train_p:.2f}%')
