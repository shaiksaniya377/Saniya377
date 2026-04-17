a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

c = abs(a - b)   
print(c)

if c < 0.001:
    print("Close")
else:
    print("Not close")
