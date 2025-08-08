numbers_as_string = input().split(", ")
numbers = []
not_a_zero = []
zero = []

for num in numbers_as_string:
    numbers.append(int(num))

for num_ in numbers:
    if num_ != 0:
        not_a_zero.append(num_)
    else:
        zero.append(num_)

numbers = not_a_zero + zero

print(numbers)

