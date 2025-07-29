beach_list = ["sand", "water", "fish", "sun"]

beach = input()
beach = beach.lower()
count = sum(beach.count(word) for word in beach_list)

print(count)