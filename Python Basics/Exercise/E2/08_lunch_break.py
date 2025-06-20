from math import ceil, floor

tv_show = input()
episode_length = int(input())
lunch_break_length = int(input())

lunch = lunch_break_length * 1 / 8
resting_time = lunch_break_length * 1 / 4
tv_show_time = (lunch_break_length
                - lunch
                - resting_time)
time_left = lunch_break_length - lunch - resting_time - episode_length
if time_left < 0:
    time_left=abs(time_left)
    time_left = ceil(time_left)
else:
    time_left = ceil(time_left)

if tv_show_time >= episode_length:
    reply = (f"You have enough time to watch {tv_show} "
             f"and left with {abs(time_left)} minutes free time.")
else:
    reply = (f"You don't have enough time to watch {tv_show}, "
             f"you need {abs(time_left)} more minutes.")
print(reply)
