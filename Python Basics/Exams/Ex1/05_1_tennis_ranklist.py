from math import floor

tournaments_count = int(input())
starting_points = int(input())

temp_points = 0
wins = 0

for _ in range(tournaments_count):
    tournament_type = input()
    
    if tournament_type == 'W':
        wins += 1
        temp_points += 2000
    
    elif tournament_type == 'F':
        temp_points += 1200
    
    else:
        temp_points += 720

final_points = starting_points + temp_points
average_points = (final_points - starting_points) / tournaments_count
wins_percentage = wins / tournaments_count * 100

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{wins_percentage:.2f}%')
