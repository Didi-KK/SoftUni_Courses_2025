movie_budget = float(input())
destination = input()
season = input()
days = int(input())

destination_cost = 0

if season == 'Winter':
    if destination == 'Dubai':
        destination_cost = 45000
    elif destination == 'Sofia':
        destination_cost = 17000
    elif destination == 'London':
        destination_cost = 24000

elif season == 'Summer':
    if destination == 'Dubai':
        destination_cost = 40000
    elif destination == 'Sofia':
        destination_cost = 12500
    elif destination == 'London':
        destination_cost = 20250

movie_expenses = days * destination_cost

if destination == 'Dubai':
    movie_expenses *= 0.70
elif destination == 'Sofia':
    movie_expenses *= 1.25

diff = abs(movie_budget - movie_expenses)

if movie_budget >= movie_expenses:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
