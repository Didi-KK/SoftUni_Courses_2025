def smallest_of_three(a: int,b: int,c: int):
    list_numbers = [a, b, c]
    return min(list_numbers)

first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_of_three(first_number, second_number,third_number))