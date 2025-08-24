people_waiting = int(input())
current_lift_state = input().split()
lift_state = []* len(current_lift_state)
MAX_PEOPLE = 4

for i in range(len(current_lift_state)):

    available_space =  MAX_PEOPLE - int(current_lift_state[i])
    people_in = min(available_space, people_waiting)
    new_lift_state = people_in + int(current_lift_state[i])
    lift_state.append(new_lift_state)
    people_waiting -= people_in

if people_waiting == 0 and any(cart < MAX_PEOPLE for cart in lift_state):
    print(f"The lift has empty spots!")
    print(*lift_state)

elif people_waiting > 0 and all(cart == MAX_PEOPLE for cart in lift_state):
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*lift_state)
else:
    print(*lift_state)
