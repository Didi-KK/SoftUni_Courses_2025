hall_rent = int(input())

statues = hall_rent * 0.70
catering = statues * 0.85
sound = catering * 0.50

expenses = hall_rent + statues + catering + sound
print(f'{expenses:.2f}')