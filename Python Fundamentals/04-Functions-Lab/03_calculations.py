def calculate(operator: str, a: float, b: float):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        if b != 0:
            return int(a / b)


math_operation = input()
first_number = int(input())
second_number = int(input())

print((calculate(math_operation, first_number, second_number)))

