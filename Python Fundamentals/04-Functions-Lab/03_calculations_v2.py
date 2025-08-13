def calculate(operator, a, b):

    return {
        "add": a + b,
        "subtract": a-b,
        "multiply": a * b,
        "divide": int(a/b)
    }.get(operator)

math_operation = input()
first_number = int(input())
second_number = int(input())

result = calculate(math_operation, first_number, second_number)
print(result)
