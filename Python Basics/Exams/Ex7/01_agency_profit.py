airline = input()
adult_ticket_qty = int(input())
kid_ticket_qty = int(input())
adult_ticket_price = float(input())
admin_fee = float(input())
kid_ticket_price = adult_ticket_price * 0.30

total_price = (adult_ticket_qty * adult_ticket_price + kid_ticket_qty * kid_ticket_price +
               (adult_ticket_qty + kid_ticket_qty) * admin_fee)
profit = 0.20 * total_price

print(f'The profit of your agency from {airline} tickets is {profit:.2f} lv.')
