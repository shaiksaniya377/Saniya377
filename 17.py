def number_of_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            print(i)
    return count

num = int(input("Enter number: "))
print("No of factors:", number_of_factors(num))
