vowels = ['a', 'o', 'u', 'e', 'i' ]

no_vowels = input()

no_vowels = "".join([ch for ch in no_vowels if ch.lower() not in vowels])
print(no_vowels)
