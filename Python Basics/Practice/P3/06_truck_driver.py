season = input()
km_per_month = float(input())

payment_per_km = 0.00
if km_per_month <= 5_000:
    if season == 'Spring' or season == 'Autumn':
        payment_per_km = 0.75
    elif season == 'Summer':
        payment_per_km = 0.90
    elif season == 'Winter':
        payment_per_km = 1.05
elif 5_000 < km_per_month <= 10_000:
    if season == 'Spring' or season == 'Autumn':
        payment_per_km = 0.95
    elif season == 'Summer':
        payment_per_km = 1.10
    elif season == 'Winter':
        payment_per_km = 1.25
elif 10_000 < km_per_month <= 20_000:
    payment_per_km = 1.45
season_payment = km_per_month * payment_per_km * 4 * 0.90
print(f'{season_payment:.2f}')
