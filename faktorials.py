def faktorials(n):
    if n == 0:
        return 1
    return n*faktorials(n-1)

print(faktorials(500))