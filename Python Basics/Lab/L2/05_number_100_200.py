number = int(input())
reply = ""
if number < 100:
    reply = "Less than 100"
elif number > 200:
    reply = "Greater than 200"
else:
    reply = "Between 100 and 200"
print(reply)
