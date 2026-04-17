def is_sorted(st):
    for i in range(len(st) - 1):
        if st[i] > st[i + 1]:
            return False
    return True

# Test list
lst = [1, 2, 3, 4, 5]

print(is_sorted(lst))
