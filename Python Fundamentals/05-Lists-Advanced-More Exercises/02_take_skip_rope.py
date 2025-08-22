digits = []
letters = []
take_string = []
skip_string = []
my_string = input()

for char in my_string:
    if char.isdigit():
        digits += char
    else:
        letters += char

take_list = [int(d) for d in digits[::2]]
skip_list = [int(d) for d in digits[1::2]]

for i in range(len(take_list)):
    take_string += letters[:take_list[i]]
    letters = letters[take_list[i]:]
    skip_string += letters[:skip_list[i]]
    letters = letters[skip_list[i]:]

print(''.join(take_string))
