total_expenses = 0
rate_per_night = 0

days = int(input())
accommodation_type = input()
rating = input()

if accommodation_type == 'room for one person':
    total_expenses = (days - 1) * 18.00
elif accommodation_type == 'apartment':
    total_expenses = (days - 1) * 25.00
    if days < 10:
        total_expenses *= 0.70
    elif days <= 15:
        total_expenses *= 0.65
    elif days > 15:
        total_expenses *= 0.50
elif accommodation_type == 'president apartment':
    total_expenses = (days - 1) * 35.00
    if days < 10:
        total_expenses *= 0.90
    elif days <= 15:
        total_expenses *= 0.85
    elif days > 15:
        total_expenses *= 0.80

if rating == 'positive':
    total_expenses *= 1.25
    print(f'{total_expenses:.2f}')
else:
    total_expenses *= 0.90
    print(f'{total_expenses:.2f}')
