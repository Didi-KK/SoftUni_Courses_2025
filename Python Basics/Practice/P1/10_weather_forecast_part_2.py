degrees_celsius = float(input())

if 26.00 <= degrees_celsius <= 35.00:
    print('Hot')
if 20.10 <= degrees_celsius <= 25.90:
    print('Warm')
if 15.00 <= degrees_celsius <= 20.00:
    print('Mild')
if 12.00 <= degrees_celsius <= 14.90:
    print('Cool')
if 5.00 <= degrees_celsius <= 11.90:
    print('Cold')
else:
    print('unknown')
