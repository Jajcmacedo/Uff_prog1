g = 0
c = 0
r = 0
s = 0
n = int(input())
for i in range(n):
    x, t = input().split()
    g += int(x)
    if t == 'C':
        c += int(x)
    elif t == 'R':
        r += int(x)
    elif t == 'S':
        s += int(x)
print(f'Total:', g, 'cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {(c * 100) / g:.2f} %')
print(f'Percentual de ratos: {(r * 100) / g:.2f} %')
print(f'Percentual de sapos: {(s * 100) / g:.2f} %')
