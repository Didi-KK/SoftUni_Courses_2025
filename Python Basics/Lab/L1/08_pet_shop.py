number_packages_dog_food = int(input())
number_packages_cat_food = int(input())
dog_food_price_per_package = 2.50
cat_food_price_per_package = 4.00
total_payable = (number_packages_dog_food * dog_food_price_per_package +
                 number_packages_cat_food * cat_food_price_per_package)

print(f"{total_payable} lv.")