from math import floor, ceil

wine_yard_area = int(input())
grape_per_sq_m = float(input())
wine_production_needed_l = int(input())
number_workers = int(input())
# grape_to_wine = 2.5

grape_qty = wine_yard_area * 40 / 100 * grape_per_sq_m
wine_produced_l = grape_qty / 2.5
production_difference = wine_production_needed_l - wine_produced_l
if wine_production_needed_l > wine_produced_l:
    reply = f'It will be a tough winter! More {floor(production_difference)} liters wine needed.'
    print(reply)
else:
    production_difference = abs(production_difference)
    wine_per_person = production_difference / number_workers
    reply_1 = f'Good harvest this year! Total wine: {floor(wine_produced_l)} liters. '
    reply_2 = f'{ceil(production_difference)} liters left -> {ceil(wine_per_person)} liters per person.'
    print(reply_1)
    print(reply_2)
