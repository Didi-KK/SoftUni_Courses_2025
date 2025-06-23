lily_age = int(input())
washing_machine_price = float(input())
single_toy_price = int(input())

toy_count = 0
bd_savings = 0

for i in range(1, lily_age + 1, 2):
    toy_count += 1
for i in range(2, lily_age + 1, 2):
    bd_savings += (10 * (i / 2) - 1)

total_saving = toy_count * single_toy_price + bd_savings
difference = total_saving - washing_machine_price

if difference >= 0:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {abs(difference):.2f}')
