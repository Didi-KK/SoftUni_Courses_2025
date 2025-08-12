def even_numbers(sequence_of_numbers):
    number = list(map(int, sequence_of_numbers.split()))
    return list(filter(lambda x: x % 2 == 0, number))

my_numbers = input()
print(even_numbers(my_numbers))
