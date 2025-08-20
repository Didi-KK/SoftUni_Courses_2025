words = input().split()
special_word = input()
palindrome_list = [word for word in words if word == word[::-1]]

special_word_count = palindrome_list.count(special_word)

print(palindrome_list)
print(f'Found palindrome {special_word_count} times')