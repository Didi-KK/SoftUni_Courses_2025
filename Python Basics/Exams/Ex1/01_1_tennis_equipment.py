from math import floor, ceil
tennis_racket_price = int(input())
tennis_racket_qty = int(input())
sneakers_qty = int(input())
sneakers_price = 1 / 6 * tennis_racket_price
total_price = (tennis_racket_price * tennis_racket_qty
               + sneakers_price * sneakers_qty)
other_equipment_price = total_price * 0.20
amount_to_be_paid = total_price + other_equipment_price
print(f"Price to be paid by Djokovic {floor(1 / 8 * amount_to_be_paid)}")
print(f"Price to be paid by sponsors {ceil(7 / 8 * amount_to_be_paid)}")
