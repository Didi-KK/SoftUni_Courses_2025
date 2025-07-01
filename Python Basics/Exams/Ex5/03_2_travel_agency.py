destination = input()
travel_package = input()
vip_member = input()
vacation_days = int(input())
cost_per_day = 0.0
vacation_cost = 0.0
is_entry_valid = False

if destination == 'Bansko' or destination == 'Borovets':
    if travel_package== 'noEquipment' or travel_package == 'withEquipment':
        is_entry_valid = True
if destination == 'Varna' or destination == 'Burgas':
    if travel_package == 'noBreakfast' or travel_package == 'withBreakfast':
        is_entry_valid = True

if destination == 'Bansko' or destination == 'Borovets':
    if travel_package == 'noEquipment':
        cost_per_day = 80.0
        if vip_member == 'yes':
            cost_per_day *= 0.95
    elif travel_package == 'withEquipment':
        cost_per_day = 100.0
        if vip_member == 'yes':
            cost_per_day *= 0.90

elif destination == 'Varna' or destination == 'Burgas':
     if travel_package == 'noBreakfast':
        cost_per_day = 100.0
        if vip_member == 'yes':
            cost_per_day *= 0.93
     elif travel_package == 'withBreakfast':
        cost_per_day = 130.0
        if vip_member == 'yes':
            cost_per_day *= 0.88

vacation_cost = vacation_days * cost_per_day

if vacation_days > 7:
    vacation_cost -= cost_per_day
if vacation_days < 1:
    print(f'Days must be positive number!')
elif is_entry_valid:
    print(f'The price is {vacation_cost:.2f}lv! Have a nice time!')
else:
    print(f'Invalid input!')
