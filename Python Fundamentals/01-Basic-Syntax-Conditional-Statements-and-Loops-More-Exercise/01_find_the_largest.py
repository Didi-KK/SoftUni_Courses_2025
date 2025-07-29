number = input()
digits = list(number)

for i in range(len(digits)):
    for j in range(i + 1, len(digits)):
        if digits[i] < digits[j]:
            digits[i], digits[j] = digits[j], digits[i]

largest_number = ''.join(digits)

print(largest_number)