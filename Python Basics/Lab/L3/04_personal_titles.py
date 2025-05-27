age = float(input())
sex = input()
title = ""

if sex == "m":

    if age >= 16:
        title = "Mr."

    else:
        title = "Master"

if sex == "f":

    if age >= 16:
        title = "Ms."

    else:
        title = "Miss"

print(title)
