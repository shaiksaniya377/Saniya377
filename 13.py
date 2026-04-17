nums = [1, 1, 2, 3, 4, 3, 0, 0]
unique = []

for i in nums:
    if i not in unique:
        unique.append(i)

print("Original list:", nums)
print("List after removing duplicates:", unique)
