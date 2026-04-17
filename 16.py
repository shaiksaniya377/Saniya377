def First_diff(s1, s2):
    n = min(len(s1), len(s2))
    
    for i in range(n):
        if s1[i] != s2[i]:
            return i   
    if len(s1) != len(s2):
        return n   
    return -1   


s1 = input("Enter string1: ")
s2 = input("Enter string2: ")

result = First_diff(s1, s2)


if result == -1:
    print("Both are identical")
else:
    print("Strings differ at position:", result)
