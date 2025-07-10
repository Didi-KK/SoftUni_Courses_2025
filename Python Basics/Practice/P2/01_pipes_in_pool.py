pool_volume: int = int(input())
pipe_one_flow_per_h = int(input())
pipe_two_flow_per_h = int(input())
hours_worked = float(input())

pipe_one = hours_worked * pipe_one_flow_per_h
pipe_two = hours_worked * pipe_two_flow_per_h

volume_filled = pipe_one + pipe_two
volume_filled_percentage = volume_filled / pool_volume * 100

volume_p1 = pipe_one / volume_filled * 100
volume_p2 = pipe_two / volume_filled * 100

if volume_filled <= pool_volume:
    reply = f'The pool is {volume_filled_percentage :.2f}% full. Pipe 1: {volume_p1:.2f}%. Pipe 2: {volume_p2:.2f}%.'
    print(reply)
else:
    reply = f'For {hours_worked:.2f} hours the pool overflows with {(volume_filled - pool_volume):.2f} liters.'
    print(reply)
