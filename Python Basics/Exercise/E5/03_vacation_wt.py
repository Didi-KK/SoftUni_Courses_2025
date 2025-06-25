needed_money = float(input())
owned_money = float(input())

days_counter = 0
spending_counter = 0

while True:
    if owned_money < needed_money and spending_counter < 5:
    
        command = input()
        money = float(input())
        days_counter += 1
    
        if command == 'save':
            owned_money += money
            spending_counter = 0
            if owned_money >= needed_money:
                print(f'You saved the money for {days_counter} days.')
                break
            
        elif command == 'spend':
            owned_money -= money
            spending_counter += 1
            if owned_money < 0:
                owned_money = 0
            elif spending_counter == 5:
                print('You can\'t save the money.')
                print(days_counter)
                break
            
