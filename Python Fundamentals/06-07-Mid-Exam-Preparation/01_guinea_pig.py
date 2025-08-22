food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000


guinea_pig_fed = True

for day in range (1, 30 + 1):

    food -= 300
    if food <= 0:
        guinea_pig_fed = False
        break
    if day % 2 == 0:
        hay -= food * 0.05
        if hay <= 0:
            guinea_pig_fed = False
            break
    if day % 3 == 0:
        cover -= weight / 3
        if cover <= 0:
            guinea_pig_fed = False
            break


if not guinea_pig_fed:
    print("Merry must go to the pet store!")

else:
    print(f"Everything is fine! Puppy is happy! "
          f"Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")