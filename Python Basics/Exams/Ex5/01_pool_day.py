from math import ceil

people = int(input())
entry_fee = float(input())
sunbed_fee = float(input())
umbrela_fee = float(input())

umbrela_count = people / 2
sunbed_count = 0.75 * people
expenses = people * entry_fee +  ceil(sunbed_count) * sunbed_fee + ceil(umbrela_count) * umbrela_fee

print(f'{expenses:.2f} lv.')
