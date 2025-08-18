number_of_electrons = int(input())
shells =[]

current_shell = 1
while number_of_electrons > 0:
    electrons_in_current_shell = 2 * current_shell ** 2
    if electrons_in_current_shell > number_of_electrons:
        shells.append(number_of_electrons)
        break
    shells.append(electrons_in_current_shell)
    number_of_electrons -= electrons_in_current_shell
    current_shell +=1
print(shells)