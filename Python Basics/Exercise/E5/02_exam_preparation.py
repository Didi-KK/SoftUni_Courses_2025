failed_threshold = int(input())

failed_times = 0
grades_total = 0
solved_problems = 0
last_problem = ''
has_failed = True

while failed_times < failed_threshold:
    
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break
    
    problem_grade = int(input())
    
    if problem_grade <= 4:
        failed_times += 1

    grades_total += problem_grade
    solved_problems += 1
    last_problem = problem_name
if has_failed:
    print(f'You need a break, {failed_times} poor grades.')

else:
    average_score = grades_total / solved_problems
    print(f'Average score: {average_score:.2f}'
          f'\nNumber of problems: {solved_problems}'
          f'\nLast problem: {last_problem}')
