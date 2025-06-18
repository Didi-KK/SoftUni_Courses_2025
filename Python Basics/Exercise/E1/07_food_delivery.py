price_chicken_menu = 10.35
price_fish_menu = 12.40
price_vegetarian_menu = 8.15
delivery_charge = 2.50

number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

chicken_menus_cost = price_chicken_menu * number_of_chicken_menus
fish_menus_cost = price_fish_menu * number_of_fish_menus
vegetarian_menus_cost = price_vegetarian_menu * number_of_vegetarian_menus

total_order_price = chicken_menus_cost + fish_menus_cost + vegetarian_menus_cost
desert_price = total_order_price * 0.20
food_order_cost = total_order_price + desert_price + delivery_charge

print(f"{food_order_cost:.2f}")
# print(float(f"{food_order_cost}"))
