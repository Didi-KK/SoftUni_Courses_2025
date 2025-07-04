aluminum_windows_price = 0
aluminum_windows_qty = int(input())
aluminum_windows_type = input()
delivery_type = input()

if aluminum_windows_qty < 10:
    print(f'Invalid order')
    quit()

if aluminum_windows_type == '90X130':
    aluminum_windows_price = 110
    if aluminum_windows_qty > 60:
        aluminum_windows_price *= 0.92
    elif aluminum_windows_qty > 30:
        aluminum_windows_price *= 0.95


elif aluminum_windows_type == '100X150':
    aluminum_windows_price = 140
    if aluminum_windows_qty > 80:
        aluminum_windows_price *= 0.90
    elif aluminum_windows_qty > 40:
        aluminum_windows_price *= 0.94

elif aluminum_windows_type == '130X180':
    aluminum_windows_price = 190
    if aluminum_windows_qty > 50:
        aluminum_windows_price *= 0.88
    elif aluminum_windows_qty > 20:
        aluminum_windows_price *= 0.93

elif aluminum_windows_type == '200X300':
    aluminum_windows_price = 250
    if aluminum_windows_qty > 50:
        aluminum_windows_price *= 0.86
    elif aluminum_windows_qty > 25:
        aluminum_windows_price *= 0.91

total_price = aluminum_windows_price * aluminum_windows_qty

if delivery_type == 'With delivery':
    total_price += 60
    if aluminum_windows_qty > 99:
        total_price *= 0.96
    print(f'{total_price:.2f} BGN')
else:
    if aluminum_windows_qty > 99:
        total_price *= 0.96
    print(f'{total_price:.2f} BGN')
