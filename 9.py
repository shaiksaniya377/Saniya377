s1 = input("Enter first word: ")
s2 = input("Enter second word: ")

c = ""

if len(s1) == len(s2):
    print("Length is same")
    
    for i in range(len(s1)):
        c = c + s1[i] + s2[i]
    
    print(c)
else:
    print("Enter appropriate words (same length)")
