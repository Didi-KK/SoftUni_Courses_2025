jumps_count = 0
failed_count = 0

is_target_achieved = False

high_jump_target = int(input())
current_target = high_jump_target - 30

while True:
    jumps_count += 1
    current_high_jump = int(input())

    if current_high_jump > current_target:

        if current_target >= high_jump_target:
            is_target_achieved = True
            break
        current_target += 5
        failed_count = 0

    else:
        failed_count += 1
        if failed_count >= 3:
            break

if is_target_achieved:
    print(f"Tihomir succeeded, he jumped over {current_target}cm after {jumps_count} jumps.")
else:
    print(f"Tihomir failed at {current_target}cm after {jumps_count} jumps.")
