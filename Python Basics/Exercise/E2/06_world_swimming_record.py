record_sec = float(input())
distance_meters = float(input())
time_per_meter = float(input())

delayed_time = distance_meters // 15 * 12.5

total_time = distance_meters * time_per_meter + delayed_time

if record_sec > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    difference = record_sec - total_time
    print(f"No, he failed! He was {abs(difference):.2f} seconds slower.")
