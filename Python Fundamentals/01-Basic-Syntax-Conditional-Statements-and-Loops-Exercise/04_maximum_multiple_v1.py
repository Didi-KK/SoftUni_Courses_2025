divisor = int(input())
boundary = int(input())
digit=()
for digit in range(boundary, divisor -1, -1):
    if digit % divisor == 0:
        break
print(digit)

