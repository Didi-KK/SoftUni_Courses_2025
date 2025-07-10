vacation_days_qty = int(input())

work_day_t = 63
vacation_day_t = 127
tom_play_time = 30000

work_day_qty = 365 - vacation_days_qty
total_play_time = vacation_days_qty * vacation_day_t + work_day_qty * work_day_t
total_play_time_h = total_play_time // 60
total_play_time_min = total_play_time % 60

if total_play_time <= tom_play_time:
    time_left = tom_play_time - total_play_time
    time_left_h = time_left // 60
    time_left_min = time_left % 60
    reply_one = f"Tom sleeps well"
    reply_two = f"{time_left_h} hours and {time_left_min} minutes less for play"
    print(reply_one)
    print(reply_two)

else:
    time_overplayed = total_play_time - tom_play_time
    time_overplayed_h = time_overplayed // 60
    time_overplayed_min = time_overplayed % 60
    reply_one = f'Tom will run away'
    reply_two = f"{time_overplayed_h} hours and {time_overplayed_min} minutes more for play"
    print(reply_one)
    print(reply_two)
