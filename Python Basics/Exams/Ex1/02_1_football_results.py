wins = 0
losses = 0
draws = 0
first_game_score = input()
second_game_score = input()
third_game_score = input()

for score in (first_game_score, second_game_score, third_game_score):
    team_goals, opponent_goals = [int(el) for el in score.split(':')]
    if team_goals > opponent_goals:
        wins += 1
    elif team_goals == opponent_goals:
        draws += 1
    else:
        losses += 1

print(f'Team won {wins} games.\nTeam lost {losses} games.\nDrawn games: {draws}')