hour_of_the_day = int(input())
day_of_the_week = input()
reply = ""
if 10 <= hour_of_the_day <= 18:
    if (day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or day_of_the_week == "Wednesday"
    or day_of_the_week == "Thursday" or day_of_the_week == "Friday" or day_of_the_week == "Saturday"):
        reply = "open"

    elif day_of_the_week == "Sunday":
        reply = "closed"

else:
    reply="closed"

print(reply)

