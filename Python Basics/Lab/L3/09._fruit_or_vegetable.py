fruit_or_vegetable = input()
reply =""

if (fruit_or_vegetable == "banana" or fruit_or_vegetable == "apple" or fruit_or_vegetable == "kiwi"
    or fruit_or_vegetable == "cherry" or fruit_or_vegetable == "lemon" or fruit_or_vegetable == "grapes"):
    reply="fruit"

elif (fruit_or_vegetable == "tomato" or fruit_or_vegetable == "cucumber" or fruit_or_vegetable =="pepper"
    or fruit_or_vegetable == "carrot"):
    reply="vegetable"

else:
    reply="unknown"

print(reply)