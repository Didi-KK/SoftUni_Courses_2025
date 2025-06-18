price_per_package_pens = 5.80
price_per_package_markers = 7.20
price_per_liter_wood_detergent = 1.20

number_of_packages_pens = int(input())
number_of_packages_markers = int(input())
liters_of_wood_detergent = int(input())
custom_discount = int(input())

total_price_for_pens = price_per_package_pens * number_of_packages_pens
total_price_for_markers = price_per_package_markers * number_of_packages_markers
total_price_for_wood_detergent = price_per_liter_wood_detergent * liters_of_wood_detergent
total_price_for_materials = total_price_for_pens + total_price_for_markers + total_price_for_wood_detergent
total_price_payable = total_price_for_materials * (100 - custom_discount) / 100

print(total_price_payable)
