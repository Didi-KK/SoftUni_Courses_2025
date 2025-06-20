puzzle_price = 2.60
talking_doll_price = 3.00
teddy_bear_price = 4.10
minion_price = 8.20
toy_truck_price = 2.00

vacation_cost = float(input())
puzzle_qty = int(input())
talking_doll_qty = int(input())
teddy_bear_qty = int(input())
minion_qty = int(input())
toy_truck_qty = int(input())

toys_qty = puzzle_qty + talking_doll_qty + teddy_bear_qty + minion_qty + toy_truck_qty

toys_cost = (
    puzzle_qty * puzzle_price
    + talking_doll_qty * talking_doll_price
    + teddy_bear_qty * teddy_bear_price
    + minion_qty * minion_price
    + toy_truck_qty * toy_truck_price
)

if toys_qty >= 50:
    discount = 25 / 100
else:
    discount = 0

toys_cost_payable = toys_cost - toys_cost * discount
rent = toys_cost_payable * 10 / 100
profit = toys_cost_payable - rent
money_difference = profit - vacation_cost
if profit >= vacation_cost:
    print(f"Yes! {abs(money_difference):.2f} lv left.")
else:
    print(f"Not enough money! {abs(money_difference):.2f} lv needed.")
