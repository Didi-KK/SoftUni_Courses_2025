basketball_fee_per_anum = int(input())

sneakers_price = basketball_fee_per_anum * (1 - 0.40)
outfit_price = sneakers_price * (1 - 0.20)
ball_price = outfit_price * 1 / 4
accessories_price = ball_price * 1 / 5
total_expenses = basketball_fee_per_anum + sneakers_price + outfit_price + ball_price + accessories_price

print(total_expenses)
