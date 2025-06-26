judges = int(input())

all_presentation_grades = 0
presentation_count = 0

while True:
    presentation = input()
    if presentation == 'Finish':
        break
    presentation_grade = 0
    for _ in range(judges):
        grade = float(input())
        presentation_grade += grade
        
    average_grade_for_presentation = presentation_grade / judges
        
    print(f'{presentation} - {average_grade_for_presentation:.2f}.')
    
    presentation_count += 1
    all_presentation_grades += average_grade_for_presentation
    
average_mark = all_presentation_grades / presentation_count
print(f'Student\'s final assessment is {average_mark:.2f}.')