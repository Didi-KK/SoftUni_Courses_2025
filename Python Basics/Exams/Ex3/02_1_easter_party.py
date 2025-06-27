guests = int(input())
cover = float(input())
budget = float(input())

cake = budget * 0.10

if guests < 10:
    cover = cover
elif guests <= 15:
    cover *= 0.85
elif guests <= 20:
    cover *= 0.80
elif guests > 20:
    cover *= 0.75

expenses = cake + guests * cover
diff = budget - expenses
if expenses <= budget:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {abs(diff):.2f} leva needed.')
