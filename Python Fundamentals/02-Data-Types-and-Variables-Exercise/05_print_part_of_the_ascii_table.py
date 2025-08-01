start_index = int(input())
end_index = int(input())

for digits in range(start_index, end_index + 1):
    if digits == end_index:
        print(chr(digits))
    else:
        print(chr(digits), end=" ")
