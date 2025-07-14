budget = float(input())
category = input()
people = int(input())
ticket = 0.00
transport = 0.00
expenses = 0.00
if category == 'VIP':
    ticket = 499.99
else:
    ticket = 249.99
if people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.60
elif 10 <= people <= 24:
    transport = budget * 0.50
elif 25 <= people <= 49:
    transport = budget * 0.40
else:
    transport = budget * 0.25
expenses = people * ticket + transport
difference = abs(budget - expenses)
if budget >= expenses:
    reply=f'Yes! You have {difference:.2f} leva left.'
else:
    reply=f'Not enough money! You need {difference:.2f} leva.'
print(reply)