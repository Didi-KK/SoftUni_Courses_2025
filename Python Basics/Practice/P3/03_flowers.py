chrysanthemums_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0.00
roses_price = 0.00
tulips_price = 0.00
if season == 'Spring' or season == 'Summer':
    chrysanthemums_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50

elif season == 'Autumn' or season == 'Winter':
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

if holiday == 'Y':
    chrysanthemums_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15

bouquet_price = (chrysanthemums_number * chrysanthemums_price
                 + roses_number * roses_price +
                 tulips_number * tulips_price)
if tulips_number > 7 and season == 'Spring':
    bouquet_price *= 0.95
elif roses_number >= 10 and season == "Winter":
    bouquet_price *=0.90
flower_number = chrysanthemums_number + roses_number + tulips_number
if flower_number > 20:
    bouquet_price *= 0.80
bouquet_price = bouquet_price +2.00
print(f'{bouquet_price:.2f}')