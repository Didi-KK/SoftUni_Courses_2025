sequence_of_integers = list(map(int, input().split()))
average_sequence_value = sum(sequence_of_integers) / len(sequence_of_integers)

greater_than_average = []

for number in sequence_of_integers:
    if number > average_sequence_value:
        greater_than_average.append(number)


if not greater_than_average:
    print("No")
else:
    greater_than_average = sorted(greater_than_average, reverse=True)
    print(* greater_than_average[0:5])
