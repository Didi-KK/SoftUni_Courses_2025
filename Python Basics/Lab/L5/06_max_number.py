from sys import maxsize
max_number = - maxsize
while True:
    text = input()
    if text == 'Stop':
        break

    number = int(text)
    
    if number > max_number:
        max_number = number
        
print(max_number)



