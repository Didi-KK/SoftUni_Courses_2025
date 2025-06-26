unsuccessful_shots = 0
successful_shots = 0

starting_points = 301

players_name = input()
entry = input()
while entry != 'Retire':
    
    points = int(input())
    
    if starting_points > 0:
        scored_points = 0
        if entry == 'Single':
            scored_points = points
            if scored_points <= starting_points:
                successful_shots += 1
                starting_points -= scored_points
            else:
                unsuccessful_shots += 1
        elif entry == 'Double':
            scored_points = points * 2
            if scored_points <= starting_points:
                successful_shots += 1
                starting_points -= scored_points
            else:
                unsuccessful_shots += 1
        elif entry == 'Triple':
            scored_points = points * 3
            if scored_points <= starting_points:
                successful_shots += 1
                starting_points -= scored_points
            else:
                unsuccessful_shots += 1
        if starting_points == 0:
            print(f'{players_name} won the leg with {successful_shots} shots.')
            break
    entry = input()
else:
    print(f'{players_name} retired after {unsuccessful_shots} unsuccessful shots.')
