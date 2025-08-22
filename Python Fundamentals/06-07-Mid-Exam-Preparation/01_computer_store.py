total_price_no_tax = 0

while True:
    command = input()

    if command == "regular" or command == "special":
        if total_price_no_tax == 0:
            print("Invalid order!")
            exit()
        break

    price = float(command)
    if price < 0:
        print("Invalid price!")
        continue

    total_price_no_tax += price
    if total_price_no_tax == 0:
        print("Invalid order!")
        exit()

total_tax = total_price_no_tax * 0.20
total_price_incl_tax = total_price_no_tax + total_tax

if command == "special":
    total_price_incl_tax *= 0.90

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total_price_no_tax:.2f}$")
print(f"Taxes: {total_tax:.2f}$")
print("-----------")
print(f"Total price: {total_price_incl_tax:.2f}$")
