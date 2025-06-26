competition_stage = input()
ticket_type = input()
ticket_qty = int(input())
picture_with_trophy = input()
ticket_price = 0.00
add_picture = 0.00

if competition_stage == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_price = 55.50
    elif ticket_type == 'Premium':
        ticket_price = 105.20
    elif ticket_type == 'VIP':
        ticket_price = 118.90
elif competition_stage == 'Semi final':
    if ticket_type == 'Standard':
        ticket_price = 75.88
    elif ticket_type == 'Premium':
        ticket_price = 125.22
    elif ticket_type == 'VIP':
        ticket_price = 300.40
elif competition_stage == 'Final':
    if ticket_type == 'Standard':
        ticket_price = 110.10
    elif ticket_type == 'Premium':
        ticket_price = 160.66
    elif ticket_type == 'VIP':
        ticket_price = 400.00

all_tickets = ticket_qty * ticket_price

if picture_with_trophy == 'Y':
    if all_tickets > 4000.00:
        all_tickets = all_tickets * 0.75
    elif 2500.00 < all_tickets <= 4000.00:
        add_picture = ticket_qty * 40
        all_tickets = all_tickets * 0.90 + add_picture
    else:
        add_picture = ticket_qty * 40
        all_tickets = all_tickets + add_picture

elif picture_with_trophy == 'N':
    if all_tickets > 4000.00:
        all_tickets *= 0.75
    elif 2500.00 < all_tickets <= 4000.00:
        all_tickets *= 0.90

print(f'{all_tickets:.2f}')
