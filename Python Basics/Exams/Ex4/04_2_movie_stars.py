budget = float(input())
budget_left = budget
command = input()
no_budget = False

while command != 'ACTION':
    actor_name = command

    if len(actor_name) > 15:
        actor_remuneration = 0.20 * budget_left
    else:
        actor_remuneration = float(input())

    budget_left -= actor_remuneration

    if budget_left < 0:
        no_budget = True
        break
    command = input()

if no_budget:
    print(f'We need {abs(budget_left):.2f} leva for our actors.')
else:
    print(f'We are left with {abs(budget_left):.2f} leva.')
