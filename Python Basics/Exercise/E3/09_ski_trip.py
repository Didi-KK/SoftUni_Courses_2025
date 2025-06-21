days_to_stay = int(input())
accommodation_type = input()
rate = input()
per_night = 0.00
discount = 0.00
additional_charge = 0.00
if accommodation_type == 'room for one person':
    per_night = 18.00
if accommodation_type == 'apartment':
    per_night = 25.00
    if days_to_stay < 10:
        discount = 0.30
    elif 10 <= days_to_stay <= 15:
        discount = 0.35
    else:
        discount = 0.50
elif accommodation_type == 'president apartment':
    per_night = 35.00
    if days_to_stay < 10:
        discount = 0.10
    elif 10 <= days_to_stay <= 15:
        discount = 0.15
    else:
        discount = 0.20
if rate == 'positive':
    additional_charge = 0.25
elif rate == 'negative':
    additional_charge = -0.10
total_price = (days_to_stay - 1) * per_night * (1 - discount) * (1 + additional_charge)
print(f'{total_price:.2f}')
