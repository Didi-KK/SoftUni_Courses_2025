total_price = 0
number_of_orders = int(input())

for order in range(number_of_orders):

    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not 0.01 <= price_per_capsule <= 100.00:
        continue
    elif not 1 <= days <= 31: # if not in range(1,31+1)
        continue
    elif not 1 <= capsules_per_day <= 2000:
        continue
    else:

        price = price_per_capsule * days * capsules_per_day
        total_price += price

        print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total_price:.2f}')
