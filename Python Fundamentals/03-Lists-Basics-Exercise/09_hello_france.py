stock_items = input().split("|")
budget = float(input())

TRAIN_TICKET = 150

money_spent = 0
products = {
    "Clothes" :	50.00,
    "Shoes" :	35.00,
    "Accessories" :	20.50
}
purchased_items_price = []
for items in stock_items:
    item, price_as_string = items.split("->")
    price = float(price_as_string)

    if price <= products.get(item, 0) and price <= budget:
        budget -= price
        purchased_items_price.append(price * 1.4)
        money_spent += price


money_available = sum(purchased_items_price) + budget
profit = sum(purchased_items_price) - money_spent

print(" ".join(f"{price:.2f}" for price in purchased_items_price))
print(f"Profit: {profit:.2f}")

if money_available >= TRAIN_TICKET:
    print(f"Hello, France!")
else:
    print(f"Not enough money.")