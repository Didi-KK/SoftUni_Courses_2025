def car_time(my_time: list):
    time = 0
    for d in my_time:
        time += d
        if d == 0:
            time *= 0.8
    return time

time_to_pass = list(map(int, input().split()))
mid_idx = len(time_to_pass) // 2

left_car = time_to_pass[: mid_idx]
right_car = time_to_pass[mid_idx + 1:]
right_car.reverse()

time_left_car = car_time(left_car)
time_right_car = car_time(right_car)


if time_left_car < time_right_car:
    print(f"The winner is left with total time: {time_left_car:.1f}")
else:
    print(f"The winner is right with total time: {time_right_car:.1f}")