days_win = 0
days_lose = 0
total_money = 0

tournament_duration = int(input())

for _ in range(tournament_duration):
    daily_money = 0
    wins = 0
    losses = 0
    command = input()
    while command != 'Finish':
        sport = command
        game_result = input()
        if game_result == 'win':
            wins += 1
            daily_money += 20
        elif game_result == 'lose':
            losses += 1
        command = input()
    if wins > losses:
        daily_money *= 1.1
        days_win += 1
    else:
        days_lose += 1

    total_money += daily_money

if days_win > days_lose:
    total_money *= 1.20
    print(f'You won the tournament! Total raised money: {total_money:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {total_money:.2f}')
