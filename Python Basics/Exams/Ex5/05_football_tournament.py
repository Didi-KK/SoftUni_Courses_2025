team_score = 0
wins = 0
draws = 0
losses = 0

football_team = input()
games_played = int(input())

for _ in range(games_played):
    command = input()
    if command == 'W':
        wins += 1
        team_score += 3

    elif command == 'D':
        draws += 1
        team_score += 1
    else:
        losses += 1

if games_played == 0:
    print(f'{football_team} hasn\'t played any games during this season.')
else:
    wins_percent = wins / games_played * 100
    print(f'{football_team} has won {team_score} points during this season.\nTotal stats:\n'
          f'## W: {wins}\n## D: {draws}\n## L: {losses}\nWin rate: {wins_percent:.2f}%')
