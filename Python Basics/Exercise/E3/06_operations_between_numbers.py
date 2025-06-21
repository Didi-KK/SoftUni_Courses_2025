number_one = int(input())
number_two = int(input())
math_operation = input()

result = 0.00

if math_operation == "+":
    result = number_one + number_two
elif math_operation == "-":
    result = number_one - number_two
elif math_operation == "*":
    result = number_one * number_two
elif math_operation == "%" and number_two != 0:
    result = number_one % number_two
elif math_operation == "/" and number_two != 0:
        result = number_one / number_two

if result % 2 == 0:
    odd_or_even = "even"
else:
    odd_or_even = "odd"
    
if number_two == 0 and math_operation == "/":
    reply = f"Cannot divide {number_one} by zero"
elif number_two == 0 and math_operation == "%":
    reply = f"Cannot divide {number_one} by zero"
elif math_operation =="%":
    reply = f"{number_one} {math_operation} {number_two} = {result}"
elif math_operation == "+" or math_operation == "*" or math_operation == "-":
    reply = f"{number_one} {math_operation} {number_two} = {result} - {odd_or_even}"

else:
    reply = f"{number_one} {math_operation} {number_two} = {result:.2f}"

print(reply)