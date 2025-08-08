sequence_of_numbers  = input().split()
message_string = list(input())
message = ""
for i in range(len(sequence_of_numbers)):
    current_sum = sum(int(digit) for digit in sequence_of_numbers[i])
    index = current_sum % len(message_string)
    message += message_string.pop(index)

print(message)
