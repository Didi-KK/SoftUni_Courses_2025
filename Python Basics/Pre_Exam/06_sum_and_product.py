number = int(input())
is_found = False

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                sum_digits = a + b + c + d
                product_digits = a * b * c * d
                if sum_digits == product_digits and number % 10 == 5:
                    is_found = True
                    print(f'{a}{b}{c}{d}')
                    break
                elif sum_digits != 0 and product_digits // sum_digits == 3 and number % 3 == 0:
                    is_found = True
                    print(f"{d}{c}{b}{a}")
                    break
            
            if is_found:
                break
    if is_found:
        break

if not is_found:
    print("Nothing found")
