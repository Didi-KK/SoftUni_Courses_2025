from math import ceil

max_sugar = 0
max_flour = 0
total_sugar = 0
total_flour = 0

easter_bread = int(input())

for _ in range(easter_bread):
    sugar_grams = int(input())
    flour_grams = int(input())

    total_sugar += sugar_grams
    total_flour += flour_grams

    if sugar_grams > max_sugar:
        max_sugar = sugar_grams

    if flour_grams > max_flour:
        max_flour = flour_grams

sugar_packet = total_sugar / 950
flour_packet = total_flour / 750

print(f'Sugar: {ceil(sugar_packet)}')
print(f'Flour: {ceil(flour_packet)}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
