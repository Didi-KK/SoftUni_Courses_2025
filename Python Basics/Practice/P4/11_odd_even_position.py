from sys import maxsize

odd_sum = 0
odd_min = maxsize
odd_max = - maxsize
even_sum = 0
even_min = maxsize
even_max = - maxsize

n = int(input())
for d in range(1, n + 1):
    digit = float(input())
    if d % 2 != 0:
        odd_sum += digit
        if digit > odd_max:
            odd_max = digit
        if digit < odd_min:
            odd_min = digit
    
    elif d % 2 == 0:
        even_sum += digit
        if digit > even_max:
            even_max = digit
        if digit < even_min:
            even_min = digit

print(f"OddSum={odd_sum:.2f},")

if odd_min == maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == - maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_min == maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == - maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
