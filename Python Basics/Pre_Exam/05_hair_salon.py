daily_target = int(input())
daily_income = 0

while daily_income < daily_target:
    entry_data = input()
    
    if entry_data == 'closed':
        break

    if entry_data == 'haircut':
        type_of_haircut =  input()
        if type_of_haircut == 'ladies':
            daily_income += 20
        elif type_of_haircut == 'mens':
            daily_income += 15
        elif type_of_haircut == 'kids':
            daily_income += 10
            
    elif entry_data =='color':
        type_of_color = input()
        if type_of_color == 'touch up':
            daily_income += 20
        elif type_of_color == 'full color':
            daily_income += 30
    

    
if daily_income >= daily_target:
    print(f'You have reached your target for the day!\nEarned money: {daily_income}lv.')
        
else:
    diff = daily_target - daily_income
    print(f'Target not reached! You need {diff}lv. more.\nEarned money: {daily_income}lv.')
