# skumria_price_per_kg = float(input())
while True:
    skumria_price_per_kg = float(input())
    if 0.00 <= skumria_price_per_kg <= 40.00:
        break

# caca_price_per_kg = float(input())
while True:
    caca_price_per_kg = float(input())
    if 0.00 <= caca_price_per_kg <= 30.00:
        break

# palamud_kg = float(input())
while True:
    palamud_kg = float(input())
    if 0.00 <= palamud_kg <= 50.00:
        break

# safrid_kg = float(input())
while True:
    safrid_kg = float(input())
    if 0.00 <= safrid_kg <= 70.00:
        break
# midi_kg = int(input())
while True:
    midi_kg = int(input())
    if 0 <= midi_kg <= 100:
        break

palamud_price_per_kg = skumria_price_per_kg * 1.60
safrid_price_per_kg = caca_price_per_kg * 1.80
midi_price_per_kg = 7.50

palamud_cost = palamud_kg * palamud_price_per_kg
safrid_cost = safrid_kg * safrid_price_per_kg

midi_cost = midi_kg * midi_price_per_kg

total_cost = palamud_cost + safrid_cost + midi_cost

print(f'{total_cost:.2f}')
