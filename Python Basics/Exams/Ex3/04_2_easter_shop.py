eggs_sold = 0
not_enough_eggs = False
is_closed = False

eggs_in_stock = int(input())

eggs_available = eggs_in_stock

command = input()

while command != 'Close':


    store_input = command
    eggs_qty = int(input())

    if store_input == 'Buy':
        if eggs_available < eggs_qty:
            not_enough_eggs = True
            break
        else:
            eggs_available -= eggs_qty
            eggs_sold += eggs_qty
    elif store_input == 'Fill':
            eggs_available += eggs_qty

    command = input()

    if command == 'Close':
        is_closed = True
        break

if is_closed:
    print(f'Store is closed!\n{eggs_sold} eggs sold.')

if not_enough_eggs:
    print(f'Not enough eggs in store!\nYou can buy only {eggs_available}.')