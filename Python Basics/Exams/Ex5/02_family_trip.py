budget = float(input())
nights = int(input())
cost_per_night = float(input())
percent_additional_expenses = int(input())

if nights > 7:
    cost_per_night *= 0.95

additional_expenses = budget * percent_additional_expenses / 100
total_expenses = nights * cost_per_night + additional_expenses

diff = abs(budget - total_expenses)

if total_expenses <= budget:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation.')
else:
    print(f'{diff:.2f} leva needed.')
