month_of_year = input()
nights = int(input())
studio_per_night = 0.00
apartment_per_night = 0.00
discount_studio = 0.00
discount_apartment = 0.00
if month_of_year == "May" or month_of_year == "October":
    studio_per_night = 50.00
    apartment_per_night = 65.00
    if 7 < nights <= 14:
        discount_studio = 0.05
    elif nights > 14:
        discount_studio = 0.30
        discount_apartment = 0.10
elif month_of_year == "June" or month_of_year == "September":
    studio_per_night = 75.20
    apartment_per_night = 68.70
    if nights > 14:
        discount_studio = 0.20
        discount_apartment = 0.10
elif month_of_year == "July" or month_of_year == "August":
    studio_per_night = 76.00
    apartment_per_night = 77.00
    if nights > 14:
        discount_apartment = 0.10
price_studio = nights * studio_per_night * (1 - discount_studio)
price_apartment = nights * apartment_per_night * (1 - discount_apartment)
reply_studio = f"Studio: {price_studio:.2f} lv."
reply_apartment = f"Apartment: {price_apartment:.2f} lv."
print(reply_apartment)
print(reply_studio)
