from math import floor

record = float(input())
distance = float(input())
time_per_meter = float(input())
slowing_down_distance = floor(distance / 50)
slowing_down_time = slowing_down_distance * 30
personal_time = distance * time_per_meter + slowing_down_time

if personal_time < record:
    print(f'Yes! The new record is {personal_time:.2f} seconds.')

else:
    time_needed = personal_time - record
    print(f'No! He was {time_needed:.2f} seconds slower.')
