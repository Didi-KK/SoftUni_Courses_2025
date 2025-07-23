first_number = int(input())
second_number = int(input())
digit = second_number

for i in range(second_number):

    if digit % first_number == 0 and digit <= second_number:
        print(digit)
        break

    digit -= 1
