population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

equal_distribution_possible = True
if sum(population) / len(population) < minimum_wealth:
    equal_distribution_possible = False

for idx in range(len(population)):
    wealth = population[idx]
    max_wealth = max(population)
    max_idx = population.index(max_wealth)
    if wealth < minimum_wealth:
        wealth_needed = minimum_wealth - wealth
        wealth += wealth_needed
        population[idx] = wealth
        max_wealth -= wealth_needed
        population[max_idx] = max_wealth

if not equal_distribution_possible:
    print("No equal distribution possible")

else:
    print(population)

