def factorial_division(num_one: int, num_two: int):

    for fact_one in range(1, num_one):
        num_one *= fact_one

    for fact_two in range(1, num_two):
        num_two *= fact_two

    return num_one / num_two

number_one = int(input())
number_two = int(input())
result = factorial_division(number_one, number_two)
print(f"{result:.2f}")