best_payer = ''
best_player_goals = 0
entry_data = input()
while entry_data != 'END':
    player_name = entry_data
    goals_scored = int(input())
    if goals_scored > best_player_goals:
        best_player_goals = goals_scored
        best_payer = player_name
    if goals_scored >= 10:
        break
    entry_data = input()

print(f'{best_payer} is the best player!')

if best_player_goals >= 3:
    print(f'He has scored {best_player_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_player_goals} goals.')
