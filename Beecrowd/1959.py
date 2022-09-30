while True:
    n, l = [int(x) for x in input().split()]
    if 3 <= n <= 1000000 and 1 <= l <= 4000:
        break
p = n * l
print(p)
