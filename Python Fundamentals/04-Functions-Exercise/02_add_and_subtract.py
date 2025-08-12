def add_and_subtract(a: int, b: int, c: int):

    def sum_numbers(x: int, y: int):
        return x + y

    def subtract(sum_first_second: int, z: int):
        return sum_first_second - z

    sum_result = sum_numbers(a, b)
    subtract_result = subtract(sum_result, c)
    print(subtract_result)


first_num = int(input())
second_num = int(input())
third_num = int(input())
add_and_subtract(first_num, second_num, third_num)
