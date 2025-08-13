def is_palindrome(some_integers: str) -> bool:
    return some_integers == some_integers[::-1]

my_string = input().split(", ")
for my_number in my_string:
    print(is_palindrome(my_number))