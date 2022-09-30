n= int(input())
for i in range(n):
    n1, n2, n3 = [float(x) for x in input().split()]
    media = (n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5)
    print(f'{media:.1f}')
