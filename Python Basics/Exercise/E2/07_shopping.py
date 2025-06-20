peters_budget = float(input())
graphics_card_qty = int(input())
processors_qty = int(input())
ram_qty = int(input())

graphics_card_price = 250.00
processor_price = graphics_card_price * graphics_card_qty * 35 / 100
ram_price = graphics_card_price * graphics_card_qty * 10 / 100

total_cost = (
        graphics_card_qty * graphics_card_price
        + processor_price * processors_qty
        + ram_qty * ram_price
)
if graphics_card_qty > processors_qty:
    total_cost = total_cost * (1 - 15 / 100)

difference = peters_budget - total_cost
if peters_budget >= total_cost:
    print(f"You have {abs(difference):.2f} leva left!")
else:
    print(f"Not enough money! You need {abs(difference):.2f} leva more!")
