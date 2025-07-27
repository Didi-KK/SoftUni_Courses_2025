event_lower = ['coding', 'dog', 'cat', 'movie']
event_upper = ['CODING', 'CAT', 'DOG', 'MOVIE']

coffee_count = 0
while True:
    event = input()
    if event == 'END':
        break
    elif event in event_lower:
        coffee_count += 1
    elif event in event_upper:
        coffee_count += 2
    elif event not in event_lower or event not in event_upper:
        continue

if coffee_count <= 5:
    print(coffee_count)
else:
    print('You need extra sleep')