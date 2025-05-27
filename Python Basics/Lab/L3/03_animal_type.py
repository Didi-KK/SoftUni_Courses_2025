animal = input()
reply = ""
if animal == 'dog':
    reply = 'mammal'

elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    reply = 'reptile'

else:
    reply = 'unknown'

print(reply)
