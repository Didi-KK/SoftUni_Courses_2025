n = int(input())

p2_count = 0.00
p4_count = 0.00
p6_count = 0.00
p8_count = 0.00
p10_count = 0.00

for _ in range(n):
    num = int(input())
    
    if num < 200:
        p2_count += 1
    elif num < 400:
        p4_count += 1
    elif num < 600:
        p6_count += 1
    elif num < 800:
        p8_count += 1
    else:
        p10_count += 1

p2 = p2_count/n *100
p4 = p4_count/n *100
p6 = p6_count/n *100
p8 = p8_count/n *100
p10 = p10_count/n *100

print(f'{p2:.2f}%')
print(f'{p4:.2f}%')
print(f'{p6:.2f}%')
print(f'{p8:.2f}%')
print(f'{p10:.2f}%')
