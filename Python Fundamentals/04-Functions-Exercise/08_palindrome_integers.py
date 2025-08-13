def is_palindrome(positive_integers: str):
    positive_integers_list = positive_integers.split(", ")
    
    for num in positive_integers_list:
        if num == num[::-1]:
            print("True")
        else:
            print("False")

my_string = input()

is_palindrome(my_string)

