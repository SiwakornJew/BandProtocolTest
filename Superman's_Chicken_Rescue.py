def max_chickens_protected(n, k, positions):
    start = 0
    max_chickens = 0

    for end in range(n):
        while positions[end] - positions[start] > k:
            start += 1
        max_chickens = max(max_chickens, end - start + 1)

    return max_chickens


n = 5
k = 5
positions = [2, 5, 10, 12, 15]
print(max_chickens_protected(n, k, positions))
