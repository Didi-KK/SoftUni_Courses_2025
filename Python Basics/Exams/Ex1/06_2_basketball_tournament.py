wins = 0
losses = 0
total_games = 0

while True:
    tournament = input()
    if tournament == 'End of tournaments':
        break

    number_of_games = int(input())
    total_games += number_of_games
    for game in range(1, number_of_games + 1):
        own_team_points = int(input())
        opposite_team_points = int(input())
        diff = abs(own_team_points - opposite_team_points)
        if own_team_points > opposite_team_points:
            wins += 1
            print(f'Game {game} of tournament {tournament}: win with {diff} points.')
        else:
            losses += 1
            print(f'Game {game} of tournament {tournament}: lost with {diff} points.')

percent_wins = wins / total_games * 100
percent_losses = 100 - percent_wins
print(f'{percent_wins:.2f}% matches win\n{percent_losses:.2f}% matches lost')
