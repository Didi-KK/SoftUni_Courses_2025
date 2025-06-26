tickets = 0
others = 0

movie_voucher = int(input())

voucher_left = movie_voucher
command = input()
while command != 'End':
    purchase_type = command
    if len(purchase_type) > 8:
        purchase = ord(purchase_type[0]) + ord(purchase_type[1])
        if purchase <= voucher_left:
            tickets += 1
    else:
        purchase = ord(purchase_type[0])
        if purchase <= voucher_left:
            others += 1

    voucher_left -= purchase
    if voucher_left < 0:
        break
    command = input()

print(tickets)
print(others)
