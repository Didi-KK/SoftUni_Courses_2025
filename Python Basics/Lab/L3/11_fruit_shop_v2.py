type_of_fruit = input()
day_of_the_week = input()
qty_fruit = float(input())

total_price = 0
error_data = False


if (day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday"
        or day_of_the_week == "Thursday" or day_of_the_week == "Friday"):
    if type_of_fruit == "banana":
        price = 2.50
        total_price = qty_fruit * price
    elif type_of_fruit == "apple":
        price = 1.20
        total_price = qty_fruit * price
    elif type_of_fruit == "orange":
        price = 0.85
        total_price = qty_fruit * price
    elif type_of_fruit == "grapefruit":
        price = 1.45
        total_price = qty_fruit * price
    elif type_of_fruit == "kiwi":
        price = 2.70
        total_price = qty_fruit * price
    elif type_of_fruit == "pineapple":
        price = 5.50
        total_price = qty_fruit * price
    elif type_of_fruit == "grapes":
        price = 3.85
        total_price = qty_fruit * price
    else:
        error_data = True

elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    if type_of_fruit == "banana":
        price = 2.70
        total_price = qty_fruit * price
    elif type_of_fruit == "apple":
        price = 1.25
        total_price = qty_fruit * price
    elif type_of_fruit == "orange":
        price = 0.90
        total_price = qty_fruit * price
    elif type_of_fruit == "grapefruit":
        price = 1.60
        total_price = qty_fruit * price
    elif type_of_fruit == "kiwi":
        price = 3.00
        total_price = qty_fruit * price
    elif type_of_fruit == "pineapple":
        price = 5.60
        total_price = qty_fruit * price
    elif type_of_fruit == "grapes":
        price = 4.20
        total_price = qty_fruit * price
    else:
        error_data = True
else:
    error_data = True

if not error_data:
    print(f"{total_price:.2f}")
else:
    print("error")
