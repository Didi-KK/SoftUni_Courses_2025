months_count = int(input())

electricity_bill = 0.0
other_bills = 0.0

for i in range(months_count):
    new_electricity_bill = float(input())
    electricity_bill += new_electricity_bill
    other_bills += ((20 + 15 + new_electricity_bill) * 1.2)

water_bill = 20 * months_count
internet_bill = 15 * months_count

average_bills_m = (electricity_bill + other_bills + water_bill + internet_bill) / months_count

print(f'Electricity: {electricity_bill:.2f} lv'
      f'\nWater: {water_bill:.2f} lv'
      f'\nInternet: {internet_bill:.2f} lv'
      f'\nOther: {other_bills:.2f} lv'
      f'\nAverage: {average_bills_m:.2f} lv')
