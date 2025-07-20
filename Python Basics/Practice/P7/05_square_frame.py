row = int(input())
for col in range(row):
    if col == 0 or col == row-1:
        print(f'+ {(row -2)*"- "}+')
    else:
        print(f'| {(row - 2) * "- "}|')
    
