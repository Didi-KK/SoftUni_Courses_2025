from math import ceil

KM_TARGET = 1000

days_training = int(input())
km_first_day = float(input())
total_km = km_first_day
km_per_day = km_first_day
for days in range(1, days_training + 1):
    increase_percentage = int(input())
    km_per_day += increase_percentage / 100 * km_per_day
    total_km += km_per_day

diff = abs(KM_TARGET - total_km)

if total_km >= KM_TARGET:
    print(f'You\'ve done a great job running {ceil(diff)} more kilometers!')
else:
    print(f'Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers')
