gasoline_per_l = 2.22
diesel_per_l = 2.33
gas_per_l = 0.93

fuel_type = input()
fuel_qty = float(input())
club_card = input()

club_card_discount_gasoline = 0.18
club_card_discount_diesel = 0.12
club_card_discount_gas = 0.08

# Gasoline
if fuel_type == "Gasoline":
    if fuel_type == "Gasoline" and 20 > fuel_qty and club_card == "Yes":
        total_price = fuel_qty * gasoline_per_l - fuel_qty * club_card_discount_gasoline
        print(f"{total_price:.2f} lv.")
    elif fuel_type == "Gasoline" and 20 > fuel_qty and club_card == "No":
        total_price = fuel_qty * gasoline_per_l
        print(f"{total_price:.2f} lv.")
    elif fuel_type == "Gasoline" and 20 <= fuel_qty <= 25 and club_card == "Yes":
        total_price = ((fuel_qty * gasoline_per_l
                        - fuel_qty * club_card_discount_gasoline)
                       * (1 - 8 / 100))
        print(f"{total_price:.2f} lv.")
    elif fuel_type == "Gasoline" and 20 <= fuel_qty <= 25 and club_card == "No":
        total_price = ((fuel_qty * gasoline_per_l)
                       * (1 - 8 / 100))
        print(f"{total_price:.2f} lv.")
    elif fuel_type == "Gasoline" and fuel_qty > 25 and club_card == "Yes":
        total_price = ((fuel_qty * gasoline_per_l
                        - fuel_qty * club_card_discount_gasoline)
                       * (1 - 10 / 100))
        print(f"{total_price:.2f} lv.")
    elif fuel_type == "Gasoline" and fuel_qty > 25 and club_card == "No":
        total_price = ((fuel_qty * gasoline_per_l)
                       * (1 - 10 / 100))
        print(f"{total_price:.2f} lv.")

# Diesel
if fuel_type == "Diesel":
    if fuel_type == "Diesel" and 20 > fuel_qty and club_card == "Yes":
        total_price = fuel_qty * diesel_per_l - fuel_qty * club_card_discount_diesel
        print(f"{total_price:.2f} lv.")
    elif fuel_type == "Diesel" and 20 > fuel_qty and club_card == "No":
        total_price = fuel_qty * diesel_per_l
        print(f"{total_price:.2f} lv.")
    elif fuel_type == "Diesel" and 20 <= fuel_qty <= 25 and club_card == "Yes":
        total_price = ((fuel_qty * diesel_per_l
                        - fuel_qty * club_card_discount_diesel)
                       * (1 - 8 / 100))
        print(f"{total_price:.2f} lv.")
    elif fuel_type == "Diesel" and 20 <= fuel_qty <= 25 and club_card == "No":
        total_price = ((fuel_qty * diesel_per_l)
                       * (1 - 8 / 100))
        print(f"{total_price:.2f} lv.")
    elif fuel_type == "Diesel" and fuel_qty > 25 and club_card == "Yes":
        total_price = ((fuel_qty * diesel_per_l
                        - fuel_qty * club_card_discount_diesel)
                       * (1 - 10 / 100))
        print(f"{total_price:.2f} lv.")
    elif fuel_type == "Diesel" and fuel_qty > 25 and club_card == "No":
        total_price = ((fuel_qty * diesel_per_l)
                       * (1 - 10 / 100))
        print(f"{total_price:.2f} lv.")

# Gas
if fuel_type == "Gas":
    if 20 > fuel_qty:
        if club_card == "Yes":
            total_price = fuel_qty * gas_per_l - fuel_qty * club_card_discount_gas
            print(f"{total_price:.2f} lv.")
        elif club_card == "No":
            total_price = fuel_qty * gas_per_l
            print(f"{total_price:.2f} lv.")
    elif 20 <= fuel_qty <= 25:
        if club_card == "Yes":
            total_price = ((fuel_qty * gas_per_l
                            - fuel_qty * club_card_discount_gas)
                           * (1 - 8 / 100))
            print(f"{total_price:.2f} lv.")
        elif club_card == "No":
            total_price = ((fuel_qty * gas_per_l)
                           * (1 - 8 / 100))
            print(f"{total_price:.2f} lv.")
    elif fuel_qty > 25:
        if club_card == "Yes":
            total_price = ((fuel_qty * gas_per_l
                            - fuel_qty * club_card_discount_gas)
                           * (1 - 10 / 100))
            print(f"{total_price:.2f} lv.")
        elif club_card == "No":
            total_price = ((fuel_qty * gas_per_l) * (1 - 10 / 100))
            print(f"{total_price:.2f} lv.")
