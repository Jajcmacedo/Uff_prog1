while True:
    n = int(input('Informe um número de 1 a 10 para que seja gerada a tabuada:'))
    if 0 < n <= 10:
        break
x = 0
print('A tabuada de', n, 'é:')
for x in range(1, 11):
    print(n, 'X', x, '=', (n * x))
