ticket_price = 5.00
cinema_capacity = int(input())
seats_left = cinema_capacity
cinema_income = 0
command = input()
is_cinema_full = False

while command != 'Movie time!' and seats_left >= 0:
    spectators = int(command)
    seats_left -= spectators
    if seats_left < 0:
        is_cinema_full = True
        break
    if spectators % 3 == 0:
        cinema_income += spectators * ticket_price - 5.00
    else:
        cinema_income += spectators * ticket_price


    command = input()

if is_cinema_full:
    print(f'The cinema is full.')
    print(f'Cinema income - {round(cinema_income)} lv.')
else:
    print(f'There are {seats_left} seats left in the cinema.')
    print(f'Cinema income - {round(cinema_income)} lv.')
