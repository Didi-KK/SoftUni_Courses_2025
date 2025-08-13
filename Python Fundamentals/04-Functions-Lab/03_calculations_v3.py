def calculate(operator, a, b):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: int(x / y) if y != 0 else "Error: Division by zero"
    }
    return operations.get(operator, lambda x, y: "Error: Invalid operator")(a, b)

math_operation = input()
first_number = int(input())
second_number = int(input())

print((calculate(math_operation, first_number, second_number)))