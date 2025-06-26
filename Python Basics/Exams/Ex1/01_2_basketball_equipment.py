basketball_annual_fee = int(input())
sneakers_price = (1 - 0.40) * basketball_annual_fee
basketball_kit_price = (1 - 0.20) * sneakers_price
basket_ball_price = 1 / 4 * basketball_kit_price
accessories_price = 1 / 5 * basket_ball_price
amount_needed = basketball_annual_fee + sneakers_price + basketball_kit_price + basket_ball_price + accessories_price
print(f'{amount_needed:.2f}')
