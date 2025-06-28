from math import ceil

filming_time = int(input())
scenes = int(input())
scene_duration = int(input())

total_scenes_time = scenes * scene_duration
daily_preparations = filming_time * 0.15
time_needed = total_scenes_time + daily_preparations
diff = abs(filming_time - time_needed)

if time_needed <= filming_time:
    print(f'You managed to finish the movie on time! You have {ceil(diff)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {ceil(diff)} minutes.')
