my_numbers = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break
    elif command.startswith("exchange"):
        index = int(command.split()[1])
        if index in range(len(my_numbers)):
            my_numbers = my_numbers[index + 1:] + my_numbers[:index + 1]
        else:
            print("Invalid index")

    elif command.startswith("max"):
        parity = command.split()[1]
        max_number = None
        max_index = 0
        if parity == "odd":
            for index, number in enumerate(my_numbers):
                if number % 2 != 0:
                    if max_number is None or number >= max_number:
                        max_number = number
                        max_index = index

        elif parity == "even":
            for index, number in enumerate(my_numbers):
                if number % 2 == 0:
                    if max_number is None or number >= max_number:
                        max_number = number
                        max_index = index

        if max_number is None:
            print("No matches")
        else:
            print(max_index)

    elif command.startswith("min"):
        parity = command.split()[1]
        min_number = None
        min_index = 0
        if parity == "odd":
            for index, number in enumerate(my_numbers):
                if number % 2 != 0:
                    if min_number is None or number <= min_number:
                        min_number = number
                        min_index = index

        elif parity == "even":
            for index, number in enumerate(my_numbers):
                if number % 2 == 0:
                    if min_number is None or number <= min_number:
                        min_number = number
                        min_index = index

        if min_number is None:
            print("No matches")
        else:
            print(min_index)


    elif command.startswith("first"):
        count, parity = command.split()[1:]
        count = int(count)
        if count in range(1, len(my_numbers)+1) and parity == "even":
            even_list = [number for number in my_numbers if number % 2 == 0]
            print(even_list[:count])
        elif count in range(1, len(my_numbers)+1) and parity == "odd":
            odd_list = [number for number in my_numbers if number % 2 != 0]
            print(odd_list[:count])
        else:
            print("Invalid count")

    elif command.startswith("last"):
        count, parity = command.split()[1:]
        count = int(count)
        if count in range(1, len(my_numbers)+1) and parity == "even":
            even_list = [number for number in my_numbers if number % 2 == 0]
            print(even_list[- count:])
        elif count in range(1, len(my_numbers) +1) and parity == "odd":
            odd_list = [number for number in my_numbers if number % 2 != 0]
            print(odd_list[- count:])
        else:
            print("Invalid count")

print(my_numbers)
