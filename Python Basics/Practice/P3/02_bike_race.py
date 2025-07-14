juniors = int(input())
seniors = int(input())
track_type = input()

juniors_fee = 0.00
seniors_fee = 0.00
if track_type == 'trail':
    juniors_fee = 5.50
    seniors_fee = 7.00
elif track_type == 'cross-country':
    juniors_fee = 8.00
    seniors_fee = 9.50
elif track_type == 'downhill':
    juniors_fee = 12.25
    seniors_fee = 13.75
elif track_type == 'road':
    juniors_fee = 20.00
    seniors_fee = 21.50
race_fees = juniors * juniors_fee + seniors * seniors_fee
total_participants = juniors + seniors
if track_type == 'cross-country' and total_participants >= 50:
    amount_donated = race_fees * (1 - 0.25) * (1 - 0.05)
else:
    amount_donated = race_fees * (1 - 0.05)
print(f'{amount_donated:.2f}')
