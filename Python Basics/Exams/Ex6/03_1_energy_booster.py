total_price = 0
price = 0
fruit = input()

package_size = input()
package_qty = int(input())

if package_size == 'small':

    if fruit == 'Watermelon':
        price = 56.00
    elif fruit == 'Mango':
        price = 36.66
    elif fruit == 'Pineapple':
        price = 42.10
    elif fruit == 'Raspberry':
        price = 20.00

    price *= 2

elif package_size == 'big':

    if fruit == 'Watermelon':
        price = 28.70
    elif fruit == 'Mango':
        price = 19.60
    elif fruit == 'Pineapple':
        price = 24.80
    elif fruit == 'Raspberry':
        price = 15.20

    price *= 5

total_price = package_qty * price
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50

print(f'{total_price:.2f} lv.')
