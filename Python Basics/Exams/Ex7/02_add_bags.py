luggage_price = 0
luggage_above_twenty_kg = float(input())
luggage_kg = float(input())
time_to_travel = int(input())
luggage_qty = int(input())
luggage_total = luggage_qty * luggage_kg

if luggage_kg < 10.0:
    luggage_price = luggage_above_twenty_kg * 0.20
elif luggage_kg <= 20.0:
    luggage_price = luggage_above_twenty_kg * 0.50
else:
    luggage_price = luggage_above_twenty_kg

if time_to_travel < 7:
    luggage_price *= 1.40
elif time_to_travel <= 30:
    luggage_price *= 1.15
else:
    luggage_price *= 1.10

total_price = luggage_qty * luggage_price

print(f'The total price of bags is: {total_price:.2f} lv.')
