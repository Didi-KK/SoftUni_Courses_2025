speed = float(input())
speed_to_text = ""
if speed <= 10:
    speed_to_text = "slow"
elif speed <= 50:
    speed_to_text = "average"
elif speed <= 150:
    speed_to_text = "fast"
elif speed <= 1000:
    speed_to_text = "ultra fast"
else:
    speed_to_text = "extremely fast"
print(speed_to_text)
