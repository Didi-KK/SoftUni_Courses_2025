kg_veggies_price_lv = float(input())
kg_fruits_price_lv = float(input())
kg_veggies_qty = int(input())
kg_fruits_qty = int(input())

total_cost_lv = kg_veggies_price_lv * kg_veggies_qty + kg_fruits_price_lv * kg_fruits_qty
total_cost_euro = total_cost_lv / 1.94

print(f'{total_cost_euro:.2f}')

