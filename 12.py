a = "Hello,how are you today?"
b = a.split()
c = {}

print("After split:", b)

for i in range(len(b)):
    c[i] = b[i]

print(c)

print("".join(b))
