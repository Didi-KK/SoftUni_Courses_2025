hall_rent = float(input())
cake = hall_rent * 0.20
drinks = cake * 0.55
animator = 1 / 3 * hall_rent

budget = hall_rent + cake + drinks + animator
print(f'{budget}')
