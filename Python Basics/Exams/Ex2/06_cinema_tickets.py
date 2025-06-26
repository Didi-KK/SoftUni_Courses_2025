student_tickets = 0
standard_tickets = 0
kids_tickets = 0

entry = input()
while entry != 'Finish':

    movie_title = entry
    free_space = int(input())
    ticket_type = input()

    all_tickets = 0

    while ticket_type != 'End':
        all_tickets += 1

        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kids_tickets += 1

        if all_tickets >= free_space:
            break

        ticket_type = input()

    space_taken_p = all_tickets / free_space * 100

    print(f'{movie_title} - {space_taken_p:.2f}% full.')

    entry = input()
total_tickets = student_tickets + standard_tickets + kids_tickets
student_tickets_p = student_tickets / total_tickets * 100
standard_tickets_p = standard_tickets / total_tickets * 100
kids_tickets_p = kids_tickets / total_tickets * 100

print(f'Total tickets: {total_tickets}')
print(f'{student_tickets_p:.2f}% student tickets.')
print(f'{standard_tickets_p:.2f}% standard tickets.')
print(f'{kids_tickets_p:.2f}% kids tickets.')
