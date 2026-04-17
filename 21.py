def can_form(word, small):
    for ch in small:
        if small.count(ch) > word.count(ch):
            return False
    return True

word = input("Enter a word: ")
words = ["cat", "dog", "hat", "at", "go", "do"]

print("Smaller words that can be formed:")

for w in words:
    if can_form(word, w):
        print(w)
