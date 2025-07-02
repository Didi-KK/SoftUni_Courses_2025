bitcoin = int(input())
yuan = float(input())
commission = float(input())

lv_from_bitcoin = bitcoin * 1168
lv_from_yuan = yuan * 0.15 * 1.76
euros = (lv_from_bitcoin + lv_from_yuan) / 1.95 * (1 - commission / 100)

print(f'{euros:.2f}')
