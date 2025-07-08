strawberries_price = float(input())
bananas_quantity_kg = float(input())
oranges_quantity_kg = float(input())
raspberries_quantity_kg = float(input())
strawberries_quantity_kg = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

total_cost = ((strawberries_quantity_kg * strawberries_price) + (raspberries_quantity_kg * raspberries_price)
              + (oranges_quantity_kg * oranges_price) + (bananas_quantity_kg * bananas_price))
print(f'{total_cost:.2f}')
