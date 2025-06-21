exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time = exam_hour * 60 + exam_min
arrival_time = arrival_hour * 60 + arrival_min

time_difference = abs(exam_time - arrival_time)
time_difference_h = time_difference // 60
time_difference_m = time_difference % 60

timing = ''
reply = ''

if arrival_time <= exam_time:
    
    if time_difference <= 30:
        timing = 'On time'
        reply = f'{time_difference_m} minutes before the start'
    
    elif time_difference > 30:
        timing = 'Early'
        
        if time_difference < 60:
            reply = f'{time_difference_m} minutes before the start'
        elif time_difference >= 60:
            reply = f'{time_difference_h}:{time_difference_m:02d} hours before the start'

elif arrival_time > exam_time:
    timing = 'Late'
    
    if time_difference < 60:
        reply = f'{time_difference_m} minutes after the start'
    elif time_difference >= 60:
        reply = f'{time_difference_h}:{time_difference_m:02d} hours after the start'

print(timing)
print(reply)

