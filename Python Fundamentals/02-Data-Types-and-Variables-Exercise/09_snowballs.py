snowball_qty = int(input())
best_snowball_value = 0

best_snowball_weight = ()
best_snowball_time = ()
best_snowball_quality = ()

for current_snowball in range(snowball_qty):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality
    if snowball_value > best_snowball_value:
        best_snowball_value = snowball_value
        best_snowball_weight = snowball_weight
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_snowball_time} = {best_snowball_value:.0f} ({best_snowball_quality})")

