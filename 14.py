a = ["inches", "yards", "miles", "millimeters", "centimeters", "meters", "kilometers"]

b = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]

n = int(input("Enter length in feet: "))

print("\nConvert feet into:")
print("1. inches")
print("2. yards")
print("3. miles")
print("4. millimeters")
print("5. centimeters")
print("6. meters")
print("7. kilometers")

r = int(input("Enter your choice (1-7): "))

result = n * b[r - 1]

print("\nResult:")
print(n, "feet =", result, a[r - 1])
