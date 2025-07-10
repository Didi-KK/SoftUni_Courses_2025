fuel_type = input()
fuel_qty = float(input())

if fuel_type != "Diesel":
    if fuel_type != "Gasoline":
        if fuel_type != "Gas":
            reply = f"Invalid fuel!"
            print(reply)

if 25 <= fuel_qty and fuel_type == "Diesel":
    reply = f"You have enough diesel."
    print(reply)
    
if 25 <= fuel_qty and fuel_type == "Gasoline":
    reply = f"You have enough gasoline."
    print(reply)

if 25 <= fuel_qty and fuel_type == "Gas":
    reply = f"You have enough gas."
    print(reply)

if 25 > fuel_qty and fuel_type == "Diesel":
    reply = f"Fill your tank with diesel!"
    print(reply)

if 25 > fuel_qty and fuel_type == "Gasoline":
    reply = f"Fill your tank with gasoline!"
    print(reply)

if 25 > fuel_qty and fuel_type == "Gas":
    reply = f"Fill your tank with gas!"
    print(reply)

