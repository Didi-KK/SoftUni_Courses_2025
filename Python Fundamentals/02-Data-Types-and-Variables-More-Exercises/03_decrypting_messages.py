# On the first line, you will receive a key (integer).
# On the second line, you will receive n – the number of lines, which will follow.
# On the next n lines – you will receive a lower and an uppercase letter per line.
# You should add the key to each of the characters and append them to a message.
# In the end, print the decrypted message.
message = ''

decryption_key = int(input())
number_of_letters = int(input())

for letters in range(number_of_letters):

    letter = input()
    new_letter_in_num = ord(letter) + decryption_key
    new_letter = chr(new_letter_in_num)
    message += new_letter

print(message)