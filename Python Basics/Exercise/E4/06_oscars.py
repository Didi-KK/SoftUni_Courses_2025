actor_name = input()
academy_points = float(input())
number_judges = int(input())

accumulated_points = academy_points

for i in range(number_judges):
    name_judge = input()
    points_judge = float(input())
    total_points_judge = len(name_judge) * points_judge / 2
    accumulated_points += total_points_judge
    if accumulated_points > 1250.5:
        break

if accumulated_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {accumulated_points:.1f}!')
else:
    points_needed = 1250.5 - accumulated_points
    print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')
