season = input()
group_type = input()
pupil_number = int(input())
nights_number = int(input())

price_per_night = 0.00
sport_type = ''
if season == 'Winter':
    if group_type == 'boys' or group_type == 'girls':
        price_per_night = 9.60
    elif group_type == 'mixed':
        price_per_night = 10.00
    if group_type == 'girls':
        sport_type = 'Gymnastics'
    elif group_type == 'boys':
        sport_type = 'Judo'
    elif group_type == 'mixed':
        sport_type = 'Ski'

elif season == 'Spring':
    if group_type == 'boys' or group_type == 'girls':
        price_per_night = 7.20
    elif group_type == 'mixed':
        price_per_night = 9.50
    if group_type == 'girls':
        sport_type = 'Athletics'
    elif group_type == 'boys':
        sport_type = 'Tennis'
    elif group_type == 'mixed':
        sport_type = 'Cycling'
elif season == 'Summer':
    if group_type == 'boys' or group_type == 'girls':
        price_per_night = 15.00
    elif group_type == 'mixed':
        price_per_night = 20.00
    if group_type == 'girls':
        sport_type = 'Volleyball'
    elif group_type == 'boys':
        sport_type = 'Football'
    elif group_type == 'mixed':
        sport_type = 'Swimming'
            
total_price = pupil_number * nights_number * price_per_night
if pupil_number >= 50:
    total_price *= 0.50
elif 20 <= pupil_number < 50:
    total_price *= 0.85
elif 10 <= pupil_number < 20:
    total_price *= 0.95

print(f'{sport_type} {total_price:.2f} lv.')

