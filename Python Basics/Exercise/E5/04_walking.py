TARGET_STEPS = 10_000
total_steps = 0

while total_steps < TARGET_STEPS:
    entry = input()
    if entry == 'Going home':
        entry = input()
        steps = int(entry)
        total_steps += steps
        if total_steps >= TARGET_STEPS:
            print(f'Goal reached! Good job!'
                  f'\n{total_steps - TARGET_STEPS} steps over the goal!')
        else:
            print(f'{TARGET_STEPS - total_steps} more steps to reach goal.')
        break
    steps = int(entry)
    total_steps += steps
    if total_steps >= TARGET_STEPS:
        print(f'Goal reached! Good job!'
              f'\n{total_steps - TARGET_STEPS} steps over the goal!')
