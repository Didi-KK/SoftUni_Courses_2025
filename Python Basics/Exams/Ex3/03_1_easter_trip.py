destination = input()
dates = input()
nights = int(input())

cost = 0.0
if dates == '21-23':
    if destination == 'France':
        cost = 30.00
    elif destination == 'Italy':
        cost = 28.00
    elif destination == 'Germany':
        cost = 32.00
elif dates == '24-27':
    if destination == 'France':
        cost = 35.00
    elif destination == 'Italy':
        cost = 32.00
    elif destination == 'Germany':
        cost = 37.00
elif dates == '28-31':
    if destination == 'France':
        cost = 40.00
    elif destination == 'Italy':
        cost = 39.00
    elif destination == 'Germany':
        cost = 43.00
trip_cost = cost * nights
print(f'Easter trip to {destination} : {trip_cost:.2f} leva.')
