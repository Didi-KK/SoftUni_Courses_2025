donation_target = int(input())

entry_data = input()

counter = 0
cash_transaction = 0
card_transaction = 0
donations_enough = False
cash_counter = 0
card_counter = 0
donations_collected = 0

while entry_data != 'End' and donations_collected < donation_target:
    
    for_sale = int(entry_data)
    counter += 1
    
    if counter % 2 != 0:  # cash
        if for_sale <= 100:
            cash_transaction += for_sale
            cash_counter += 1
            print(f'Product sold!')
        else:
            print(f'Error in transaction!')
    
    elif counter % 2 == 0:  # card
        if for_sale > 10:
            card_transaction += for_sale
            card_counter += 1
            print(f'Product sold!')
        else:
            print(f'Error in transaction!')
    
    donations_collected = cash_transaction + card_transaction
    
    if donations_collected >= donation_target:
        donations_enough = True
        break
        
    entry_data = input()

if donations_enough:
    print(f'Average CS: {(cash_transaction / cash_counter):.2f}')
    print(f'Average CC: {(card_transaction / card_counter):.2f}')

else:
    print(f'Failed to collect required money for charity.')
