number_of_messages = int(input())

current_message = ""

for messages in range(number_of_messages):
    message = int(input())

    if message == 88:
        current_message = "Hello"
    elif message == 86:
        current_message = "How are you?"
    elif message < 88:
        current_message = "GREAT!"
    else:
        current_message = "Bye."

    print(current_message)