from sys import maxsize

min_number = maxsize
while True:
    text = input()
    if text == 'Stop':
        break
    
    number = int(text)
    
    if number < min_number:
        min_number = number

print(min_number)



