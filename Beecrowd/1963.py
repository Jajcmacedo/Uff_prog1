while True:
    a, b = [float(x) for x in input().split()]
    if 0.00 < a <= b <= 1000.00:
        break
porcentagem = ((b - a) / a) * 100
print(f'{porcentagem:.2f}%')
