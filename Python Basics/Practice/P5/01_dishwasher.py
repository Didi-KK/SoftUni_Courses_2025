detergent_bottles = int(input())

detergent_ml = detergent_bottles * 750

entry_data = input()
counter = 0
plates_counter = 0
pots_counter = 0

while entry_data != 'End':
    
    to_wash = int(entry_data)
    counter += 1
    if counter % 3 != 0:
        detergent_ml -= to_wash * 5
        plates_counter += to_wash
    else:
        to_wash = int(entry_data)
        detergent_ml -= to_wash * 15
        pots_counter += to_wash
    
    if detergent_ml < 0:
        break
    entry_data = input()

if detergent_ml >= 0:
    print(f'Detergent was enough!'
          f'\n{plates_counter} dishes and {pots_counter} pots were washed.'
          f'\nLeftover detergent {detergent_ml} ml.')
else:
    print(f'Not enough detergent, {abs(detergent_ml)} ml. more necessary!')
