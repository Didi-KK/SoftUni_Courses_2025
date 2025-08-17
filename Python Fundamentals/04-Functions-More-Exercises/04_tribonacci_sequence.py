def tribonacci(n):

    numbers = [1, 1, 2]

    while len(numbers) < n:
        next_num = numbers[-1] + numbers[-2] + numbers[-3]
        numbers.append(next_num)

    print(" ".join(map(str, numbers[:n])))

my_number = int(input())
tribonacci(my_number)