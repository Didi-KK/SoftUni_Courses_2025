total_parking_fee = 0

days_count = int(input())
hours_count = int(input())

for day in range(1, days_count +1):
    daily_parking_fee = 0
    
    for hour in range(1, hours_count +1):
        
        if day % 2 != 0 and hour % 2 == 0:
            daily_parking_fee += 1.25

        elif day % 2 == 0 and hour %2 != 0:
            daily_parking_fee += 2.50

        else:
            daily_parking_fee += 1.00
            
    print(f'Day: {day} - {daily_parking_fee:.2f} leva')
    total_parking_fee += daily_parking_fee
    
print(f'Total: {total_parking_fee:.2f} leva')

