is_prime = True
number = int(input())

for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
if is_prime:
    print(f"True")
else:
    print(f"False")
