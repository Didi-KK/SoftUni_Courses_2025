from math import floor, ceil

magnolias_price = 3.25
hyacinths_price = 4.00
roses_price = 3.50
cacti_price = 8.00

magnolias_qty = int(input())
hyacinths_qty = int(input())
roses_qty = int(input())
cacti_qty = int(input())
gift_price = float(input())

total_sale = (magnolias_qty * magnolias_price
              + hyacinths_qty * hyacinths_price
              + roses_qty * roses_price
              + cacti_qty * cacti_price)
sale_tax = total_sale * 5 / 100
sale_profit = total_sale - sale_tax
if sale_profit >= gift_price:
    money_difference = sale_profit - gift_price
    money_difference = floor(money_difference)
    reply = f"She is left with {money_difference} leva."
    print(reply)
else:
    money_difference = sale_profit - gift_price
    money_difference = ceil(abs(money_difference))
    reply = f"She will have to borrow {money_difference} leva."
    print(reply)
