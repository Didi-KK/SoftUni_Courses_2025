taxi_base_fare = 0.70
taxi_day_fare_km = 0.79
taxi_night_fare_km = 0.90
bus_day_night_fare_km_min_20 = 0.09
train_day_night_fare_km_min_100 = 0.06

km_to_travel = int(input())
time_of_the_day = input()
travel_charge = 0

if km_to_travel < 20 and time_of_the_day == 'day':
    travel_charge = taxi_base_fare + km_to_travel * taxi_day_fare_km

elif km_to_travel < 20 and time_of_the_day == 'night':
    travel_charge = taxi_base_fare + km_to_travel * taxi_night_fare_km

elif km_to_travel <100:
    travel_charge = km_to_travel * bus_day_night_fare_km_min_20

elif km_to_travel >= 100:
    travel_charge = km_to_travel * train_day_night_fare_km_min_100
    
print(f'{travel_charge:.2f}')
