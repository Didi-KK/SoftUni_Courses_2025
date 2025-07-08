product_count = 0
expenses = 0
budget = float(input())
entry_data = input()

while entry_data != 'Stop':
    product_name = entry_data
    product_price = float(input())
    product_count += 1
    if product_count % 3 == 0:
        product_price *= 0.5
        
    expenses += product_price
    budget -= product_price
    if budget < 0:
        break
    entry_data = input()
    
if entry_data == 'Stop':
    print(f'You bought {product_count} products for {expenses:.2f} leva.')
else:
    print(f'You don\'t have enough money!\nYou need {abs(budget):.2f} leva!')