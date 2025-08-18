number_of_rooms = int(input())

free_chairs = 0

for number_of_rooms in range(1, number_of_rooms+1):
    chairs_in_current_room, visitors = input().split()
    difference = len(chairs_in_current_room) - int(visitors)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {number_of_rooms}")
    free_chairs += difference
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")

