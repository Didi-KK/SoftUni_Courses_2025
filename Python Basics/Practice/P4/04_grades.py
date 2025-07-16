students_number = int(input())


num_fail = 0
num_3_4 = 0
num_4_5 = 0
num_5_6 = 0

mark_fail = 0.0
mark_3_4 = 0.0
mark_4_5 = 0.0
mark_5_6 = 0.0

total_students = 0

for i in range(students_number):
    mark = float(input())
    if mark <= 2.99:
        num_fail += 1
        mark_fail += mark
    elif mark <= 3.99:
        num_3_4 += 1
        mark_3_4 += mark
    elif mark <= 4.99:
        num_4_5 += 1
        mark_4_5 += mark
    elif mark <= 6:
        num_5_6 += 1
        mark_5_6 += mark

total_students = num_fail + num_3_4 + num_4_5 + num_5_6

num_fail_p = num_fail / total_students * 100
num_3_4_p = num_3_4 / total_students * 100
num_4_5_p = num_4_5 / total_students * 100
num_5_6_p = num_5_6 / total_students * 100

average_mark = (mark_fail + mark_3_4 + mark_4_5 + mark_5_6) / total_students

print(f'Top students: {num_5_6_p:.2f}%\nBetween 4.00 and 4.99: {num_4_5_p:.2f}%'
      f'\nBetween 3.00 and 3.99: {num_3_4_p:.2f}%\nFail: {num_fail_p:.2f}%'
      f'\nAverage: {average_mark:.2f}')
