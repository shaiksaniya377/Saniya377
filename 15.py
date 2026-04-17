def sum_digits(n):
    total = 0
    for i in n:
        total += int(i)
    return total

n = input("Enter a value: ")

result = sum_digits(n)

print("Sum of digits:", result)
