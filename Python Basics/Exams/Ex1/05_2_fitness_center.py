visitors = int(input())
total_visitors = visitors
back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake_count = 0
protein_bar_count = 0

while True:
    if visitors > 0:
        workout = input()

        if workout == 'Back':
            back_count += 1
        elif workout == 'Chest':
            chest_count += 1
        elif workout == 'Legs':
            legs_count += 1
        elif workout == 'Abs':
            abs_count += 1
        elif workout == 'Protein shake':
            protein_shake_count += 1
        elif workout == 'Protein bar':
            protein_bar_count += 1
        visitors -= 1
    if visitors == 0:
        break


workout_visitors = back_count + chest_count + legs_count + abs_count
workout_visitors_p = workout_visitors / total_visitors * 100
print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake_count} - protein shake")
print(f"{protein_bar_count} - protein bar")
print(f"{workout_visitors_p:.2f}% - work out")
print(f"{(100 - workout_visitors_p):.2f}% - protein")
