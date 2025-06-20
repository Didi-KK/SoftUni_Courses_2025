hours = int(input())
minutes = int(input())

hours_to_minutes = hours * 60
total_minutes = hours_to_minutes + minutes
interval_minutes = 15
total_minutes += 15

new_hour = total_minutes // 60
new_minutes = total_minutes % 60
if new_hour == 24:
    new_hour = 0
print(f"{new_hour}:{new_minutes:02d}")
