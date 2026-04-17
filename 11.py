import random

nums = []
count = 0
for i in range(20):
    nums.append(random.randrange(1, 100))

print("Numbers:", nums)

s = sum(nums)
avg = s / len(nums)

print("Total is:", s)
print("Average is:", avg)

nums.sort()
print("After sorting:", nums)
print("Min number:", nums[0])
print("Max number:", nums[-1])
print("Second min number:", nums[1])
print("Second max number:", nums[-2])
for n in nums:
    if n % 2 == 0:
        count += 1

print("Count of even numbers:", count)
