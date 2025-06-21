budget = float(input())
season = input()

destination = ""
accommodation = ""
expenses = 0.00

if budget <=100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        expenses = budget * 0.30
    elif season == "winter":
        accommodation = "Hotel"
        expenses = budget * 0.70
elif budget <= 1_000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        expenses = budget * 0.40
    elif season == "winter":
        accommodation = "Hotel"
        expenses = budget * 0.80
else:
    destination = "Europe"
    accommodation = "Hotel"
    expenses = budget * 0.90

vacation_location = f"Somewhere in {destination}"
vacation_type = f"{accommodation} - {expenses:.2f}"

print(vacation_location)
print(vacation_type)