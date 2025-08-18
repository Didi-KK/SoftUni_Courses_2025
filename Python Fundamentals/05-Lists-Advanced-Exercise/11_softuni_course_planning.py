lessons = input().split(', ')

while (command := input()) != 'course start':
    schedule = command.split(':')
    action = schedule[0]
    title = schedule[1]

    if action == 'Add':
        if title not in lessons:
            lessons.append(title)

    elif action == 'Insert':
        index = int(schedule[2])
        if index in range(len(lessons)) and title not in lessons:
            lessons.insert(index, title)

    elif action == 'Remove':
        exercise = f"{title}-Exercise"
        if title in lessons:
            title_idx = lessons.index(title)

            if (title_idx + 1) in range(len(lessons)) and lessons[title_idx + 1] == exercise:
                lessons.remove(exercise)

            lessons.remove(title)

    elif action == 'Swap':
        title_2 = schedule[2]

        if title in lessons and title_2 in lessons:

            title_idx = lessons.index(title)
            title_2_idx = lessons.index(title_2)
            exercise = f"{title}-Exercise"
            exercise_2 = f"{title_2}-Exercise"

            if exercise not in lessons and exercise_2 not in lessons:
                lessons[title_idx], lessons[title_2_idx] = lessons[title_2_idx], lessons[title_idx]

            elif exercise in lessons and exercise_2 in lessons:
                lessons[title_idx], lessons[title_2_idx] = lessons[title_2_idx], lessons[title_idx]
                lessons[title_idx + 1], lessons[title_2_idx + 1] = lessons[title_2_idx + 1], lessons[title_idx + 1]

            elif exercise in lessons and exercise_2 not in lessons:
                lessons[title_idx], lessons[title_2_idx] = lessons[title_2_idx], lessons[title_idx]
                lessons.insert((title_2_idx + 1), lessons.pop(title_idx + 1))

            elif exercise not in lessons and exercise_2 in lessons:
                lessons[title_idx], lessons[title_2_idx] = lessons[title_2_idx], lessons[title_idx]
                lessons.insert((title_idx + 1), lessons.pop(title_2_idx + 1))

    elif action == 'Exercise':
        exercise = f"{title}-Exercise"
        if title not in lessons:
            lessons.append(title)
            lessons.append(exercise)
        elif title in lessons and exercise not in lessons:
            title_idx = lessons.index(title)
            lessons.insert((title_idx + 1), exercise)

for i in range(1, len(lessons) + 1):
    print(f"{i}.{lessons[i - 1]}")
