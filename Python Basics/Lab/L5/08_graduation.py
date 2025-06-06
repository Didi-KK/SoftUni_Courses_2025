pupil_name = input()
total_grades = 0
year_count = 0
year_failed = 0

while year_count < 12:
    year_grade = float(input())
    
    if year_grade < 4:
        year_failed += 1
        if year_failed == 2:
            year_count += 1
            print(f'{pupil_name} has been excluded at {year_count} grade')
            break
        continue
    year_count += 1
    total_grades += year_grade
    
else:
    average_grade = total_grades / year_count
    print(f'{pupil_name} graduated. Average grade: {average_grade:.2f}')
