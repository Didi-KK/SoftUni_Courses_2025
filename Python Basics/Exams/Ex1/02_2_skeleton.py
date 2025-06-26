control_time_min = int(input())
control_time_sec = int(input())
track_length_meters = float(input())
sec_per_100_meters = int(input())
personal_time = track_length_meters / 100 * sec_per_100_meters - track_length_meters / 120 * 2.5
control_time_record_sec = control_time_min * 60 + control_time_sec
if personal_time <= control_time_record_sec:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {personal_time:.3f}.')
elif personal_time > control_time_record_sec:
    print(f'No, Marin failed! He was {(personal_time - control_time_record_sec):.3f} second slower.')
    