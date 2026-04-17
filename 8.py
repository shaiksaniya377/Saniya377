a = input("Enter a word: ")
vowels = "aeiouAEIOU"

found = False

for letter in a:
    if letter in vowels:
        found = True
        break

if found:
    print("The word contains a vowel")
else:
    print("The word does not contain vowels")
