numbers_string = input().split()
numbers_integers = [int(n) for n in numbers_string]

print(f"The minimum number is {min(numbers_integers)}")
print(f"The maximum number is {max(numbers_integers)}")
print(f"The sum number is: {sum(numbers_integers)}")
